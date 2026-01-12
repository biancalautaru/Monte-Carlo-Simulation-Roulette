import random
import matplotlib.pyplot as plt
import numpy as np
from constants import BET_TYPES, TOTAL_SLOTS
import strategies

STARTING_BANKROLL = 1000
UNIT_SIZE = 10
NUM_SPINS = 1000
NUM_SIMULATIONS = 50

STRATEGY_LIST = [
    strategies.strategy_flat,
    strategies.strategy_martingale,
    strategies.strategy_fibonacci
]

def run_simulation(strategy_func, win_prob, payout):
    bankroll = STARTING_BANKROLL
    history = [bankroll]
    current_bet_units = 1
    
    for _ in range(NUM_SPINS):
        if bankroll <= 0:
            break

        wager = current_bet_units * UNIT_SIZE
        if wager > bankroll:
            wager = bankroll
            current_bet_units = wager / UNIT_SIZE

        win = random.random() < win_prob
        
        if win:
            bankroll += wager * payout
        else:
            bankroll -= wager
        
        history.append(bankroll)
        current_bet_units = strategy_func(win, current_bet_units)
        
    return history

def analyze_and_plot():
    print(f"{'BET TYPE':<15} | {'STRATEGY':<12} | {'AVG FINAL':<10} | {'RUIN %':<8}")
    print("-" * 55)

    for bet_name, (numbers, payout) in BET_TYPES.items():
        win_prob = numbers / TOTAL_SLOTS
        
        plt.figure(figsize=(10, 6))
        
        for strat in STRATEGY_LIST:
            strat_name = strat.__name__.replace('strategy_', '')
            final_balances = []
            rep_history = []
            ruins = 0
            
            for i in range(NUM_SIMULATIONS):
                hist = run_simulation(strat, win_prob, payout)
                final_balances.append(hist[-1])
                if hist[-1] <= 0:
                    ruins += 1
                if i == 0:
                    rep_history = hist
            
            print(f"{bet_name:<15} | {strat_name:<12} | ${np.mean(final_balances):<9.0f} | {(ruins / NUM_SIMULATIONS)*100:.1f}%")
            plt.plot(rep_history, label=strat_name)

        plt.title(f"Simulation: {bet_name} (Payout {payout}:1)")
        plt.xlabel("Spins")
        plt.ylabel("Bankroll")
        plt.axhline(STARTING_BANKROLL, color='black', linestyle='--', alpha=0.3)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        filename = f"sim_{bet_name.replace(' ', '_')}.png"
        plt.savefig(f"plots/{filename}")
        plt.close()

if __name__ == "__main__":
    analyze_and_plot()
