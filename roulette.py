import numpy as np
import matplotlib.pyplot as plt
import constants as c

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
