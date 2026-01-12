from monte_carlo import run_monte_carlo
from analiza import calculate_estimates, confidence_interval_clt, plot_convergence_clt

def main():
    num_simulations = 10000
    initial_capital = 100
    max_rounds = 1000
    win_prob = 18 / 37

    ruin_indicator, rounds_played, final_capital = run_monte_carlo(num_simulations, initial_capital, max_rounds, win_prob)

    estimates = calculate_estimates(ruin_indicator, rounds_played, final_capital)
    print("Monte Carlo Estimates:")
    for k, v in estimates.items():
        print(f"  {k}: {v:.5f}")

    ci_ruin = confidence_interval_clt(ruin_indicator)
    ci_time = confidence_interval_clt(rounds_played)
    ci_capital = confidence_interval_clt(final_capital)
    
    print("\n95% Confidence Intervals:")
    print(f"  P(ruin): [{ci_ruin[0]:.5f}, {ci_ruin[1]:.5f}]")
    print(f"  E[time]: [{ci_time[0]:.5f}, {ci_time[1]:.5f}]")
    print(f"  E[capital]: [{ci_capital[0]:.5f}, {ci_capital[1]:.5f}]")

    # plot_convergence_clt(ruin_indicator, "Convergence of P(ruin) Estimate")
    # plot_convergence_clt(rounds_played, "Convergence of E[time] Estimate")
    # plot_convergence_clt(final_capital, "Convergence of E[capital] Estimate")

if __name__ == '__main__':
    main()
