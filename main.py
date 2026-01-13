import matplotlib.pyplot as plt
import numpy as np
import os
from constants import BET_TYPES, TOTAL_SLOTS
import strategies
from monte_carlo import run_monte_carlo, simulate_roulette_session
from analysis import compute_estimates, confidence_interval_clt, plot_convergence_clt

STARTING_BANKROLL = 1000
UNIT_SIZE = 10
NUM_SPINS = 10_000
NUM_SIMULATIONS = 500

STRATEGY_LIST = [
    strategies.strategy_flat,
    strategies.strategy_martingale,
    strategies.strategy_fibonacci
]

def analyze_and_plot():
    # Ensure plot directories exist
    os.makedirs("plots/sims", exist_ok=True)
    os.makedirs("plots/clt", exist_ok=True)

    print(f"{'BET TYPE':<15} | {'STRATEGY':<12} | {'AVG FINAL':<10} | {'RUIN %':<8} | {'MC EST (Capital)':<15} | {'95% CI (Capital)':<20}")
    print("-" * 100)

    initial_capital_units = STARTING_BANKROLL / UNIT_SIZE

    for bet_idx, (bet_name, (numbers, payout)) in enumerate(BET_TYPES.items()):
        win_prob = numbers / TOTAL_SLOTS
        
        plt.figure(figsize=(10, 6))
        
        for strat in STRATEGY_LIST:
            strat_name = strat.__name__.replace('strategy_', '')
            final_balances = []
            rep_history = []
            ruins = 0
            
            for i in range(NUM_SIMULATIONS):
                hist_units = simulate_roulette_session(
                    initial_capital=initial_capital_units,
                    max_rounds=NUM_SPINS,
                    win_prob=win_prob,
                    payout=payout,
                    strategy_func=strat,
                    return_history=True
                )
                
                hist_currency = [h * UNIT_SIZE for h in hist_units]                
                final_bal = hist_currency[-1]
                final_balances.append(final_bal)
                
                if final_bal <= 0:
                    ruins += 1
                if i == 0:
                    rep_history = hist_currency
            
            ruin_ind, rounds, final_caps_units = run_monte_carlo(
                num_simulations=1000,
                initial_capital=initial_capital_units,
                max_rounds=NUM_SPINS,
                win_prob=win_prob,
                payout=payout,
                strategy_func=strat
            )
            
            estimates = compute_estimates(ruin_ind, rounds, final_caps_units)
            mc_final_capital_avg = estimates["average_final_capital"] * UNIT_SIZE
            mc_capital_ci = confidence_interval_clt(final_caps_units * UNIT_SIZE)
            
            print(f"{bet_name:<15} | {strat_name:<12} | ${np.mean(final_balances):<9.0f} | {(ruins / NUM_SIMULATIONS)*100:.1f}%   | ${mc_final_capital_avg:<14.2f} | [{mc_capital_ci[0]:.0f}, {mc_capital_ci[1]:.0f}]")
            
            plt.plot(rep_history, label=strat_name)
            plot_convergence_clt(final_caps_units * UNIT_SIZE, f"plots/clt/convergence_capital_estimate_{bet_name}_{strat_name}")

        plt.title(f"Simulation: {bet_name} (Payout {payout}:1)")
        plt.xlabel("Spins")
        plt.ylabel("Bankroll")
        plt.axhline(STARTING_BANKROLL, color='black', linestyle='--', alpha=0.3)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        filename = f"plots/sims/sim_{bet_name.replace(' ', '_')}.png"
        plt.savefig(f"{filename}")
        plt.close()

if __name__ == "__main__":
    analyze_and_plot()
