import matplotlib.pyplot as plt
import numpy as np
import monte_carlo
import analysis
import strategies

def get_running_average(data):
    return np.cumsum(data) / np.arange(1, len(data) + 1)

def plot_convergence(r_flat, r_mart, r_fib):
    plt.figure(figsize=(10, 6))
    
    avg_flat = get_running_average(r_flat)
    avg_mart = get_running_average(r_mart)
    avg_fib = get_running_average(r_fib)
    
    plt.plot(avg_flat, label='flat bet', linewidth=2)
    plt.plot(avg_mart, label='martingale', linewidth=2)
    plt.plot(avg_fib, label='fibonacci', linewidth=2)
    
    plt.xlabel('number of simulations')
    plt.ylabel('estimated probability of ruin')
    plt.title('convergence of ruin probability estimates')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('graph_convergence_ruin.png')
    plt.close()
    print("generated: graph_convergence_ruin.png")

def plot_time_histogram(t_flat, t_mart, t_fib):
    plt.figure(figsize=(10, 6))
    
    plt.hist(t_flat, bins=30, alpha=0.5, label='flat bet', density=True)
    plt.hist(t_mart, bins=30, alpha=0.5, label='martingale', density=True)
    plt.hist(t_fib, bins=30, alpha=0.5, label='fibonacci', density=True)
    
    plt.xlabel('rounds played before ruin/stop')
    plt.ylabel('frequency (density)')
    plt.title('distribution of session duration')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('graph_time_histogram.png')
    plt.close()
    print("generated: graph_time_histogram.png")

def compare_strategies():
    print("\n" + "="*80)
    print(" experiment: flat bet vs. martingale vs. fibonacci")
    print("="*80)
    
    n = 5000
    c0 = 100
    max_rounds = 1000
    prob = 18/37
    
    print(f"1. running flat bet ({n} simulations)")
    r_flat, t_flat, c_flat = monte_carlo.run_monte_carlo(
        n, c0, max_rounds, prob, 
        strategy_func=strategies.strategy_flat
    )
    est_flat = analysis.compute_estimates(r_flat, t_flat, c_flat)
    
    print(f"2. running martingale ({n} simulations)")
    r_mart, t_mart, c_mart = monte_carlo.run_monte_carlo(
        n, c0, max_rounds, prob, 
        strategy_func=strategies.strategy_martingale
    )
    est_mart = analysis.compute_estimates(r_mart, t_mart, c_mart)

    print(f"3. running fibonacci ({n} simulations)")
    r_fib, t_fib, c_fib = monte_carlo.run_monte_carlo(
        n, c0, max_rounds, prob, 
        strategy_func=strategies.strategy_fibonacci
    )
    est_fib = analysis.compute_estimates(r_fib, t_fib, c_fib)
    
    print("\ncomparative results:")
    print(f"{'metric':<22} | {'flat bet':<12} | {'martingale':<12} | {'fibonacci':<12}")
    print("-" * 70)
    print(f"{'ruin probability':<22} | {est_flat['ruin_probability']:.4f}       | {est_mart['ruin_probability']:.4f}       | {est_fib['ruin_probability']:.4f}")
    print(f"{'avg time (rounds)':<22} | {est_flat['average_time_to_stop']:.1f}       | {est_mart['average_time_to_stop']:.1f}       | {est_fib['average_time_to_stop']:.1f}")
    print(f"{'avg final capital':<22} | {est_flat['average_final_capital']:.1f}       | {est_mart['average_final_capital']:.1f}       | {est_fib['average_final_capital']:.1f}")

    print("\ngenerating graphs")
    plot_convergence(r_flat, r_mart, r_fib)
    plot_time_histogram(t_flat, t_mart, t_fib)

if __name__ == "__main__":
    compare_strategies()
