import numpy as np
import matplotlib.pyplot as plt
import constante as c

SIMPLE_BETS_MAP = {
    "red": c.RED_BETS,
    "black": c.BLACK_BETS,
    "even": c.EVEN_BETS,
    "odd": c.ODD_BETS,
    "low": c.LOW_BETS,
    "high": c.HIGH_BETS,
    "snake": c.SNAKE_BETS
}

def get_winning_numbers(bet_type, bet_data):
    if bet_type == "straight":
        return [bet_data]
    
    if bet_type == "dozen":
        return c.DOZEN_BETS[bet_data - 1]
        
    if bet_type == "column":
        return c.COLUMN_BETS[bet_data - 1]
        
    if bet_type in ["red_black", "even_odd", "low_high"]:
        return SIMPLE_BETS_MAP[bet_data]
        
    if bet_type == "snake":
        return c.SNAKE_BETS
        
    # For split, street, corner, double_street, basket, first_four, top_line
    # we assume bet_data is the list of winning numbers.
    return bet_data

def simulate_roulette(num_simulations, bet_type, bet_data=None):
    payout = c.BET_TYPES[bet_type]
    winning_numbers = get_winning_numbers(bet_type, bet_data)
    
    results = np.random.randint(0, 37, size=num_simulations)
    winnings = np.where(np.isin(results, winning_numbers), payout, -1)
    
    return winnings

def calculate_average_win(winnings):
    return np.mean(winnings)

def calculate_cumulative_average(winnings):
    return np.cumsum(winnings) / np.arange(1, len(winnings) + 1)

def plot_convergence(winnings, expected_value, title):
    averages = calculate_cumulative_average(winnings)
    
    plt.figure(figsize=(10, 6))
    plt.plot(averages, label="Estimare Monte Carlo")
    plt.axhline(expected_value, linestyle="--", color="red", label="Valoare Teoretică")

    plt.xlabel("Simulări")
    plt.ylabel("Media Câștigurilor")
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")

def main():
    n_sims = 100000
    expected_val = -1 / 37

    print("--- Roulette Simulation ---")

    print("1. Bet on RED")
    res_red = simulate_roulette(n_sims, "red_black", "red")
    print(f"   Estimated Average Win: {calculate_average_win(res_red):.5f}")

    print("\n2. Bet on STRAIGHT (7)")
    res_7 = simulate_roulette(n_sims, "straight", 7)
    print(f"   Estimated Average Win: {calculate_average_win(res_7):.5f}")

    print("\n3. Bet on STREET ([1, 2, 3])")
    res_street = simulate_roulette(n_sims, "street", [1, 2, 3])
    print(f"   Estimated Average Win: {calculate_average_win(res_street):.5f}")
    
    print("\n4. Bet on SNAKE")
    res_snake = simulate_roulette(n_sims, "snake")
    print(f"   Estimated Average Win: {calculate_average_win(res_snake):.5f}")

    print("\n5. Bet on CORNER ([1, 2, 4, 5])")
    res_corner = simulate_roulette(n_sims, "corner", [1, 2, 4, 5])
    print(f"   Estimated Average Win: {calculate_average_win(res_corner):.5f}")

if __name__ == '__main__':
    main()
