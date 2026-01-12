import numpy as np

def simulate_roulette_session(initial_capital, max_rounds, win_prob=18/37):
    capital = initial_capital

    for round_num in range(1, max_rounds + 1):
        if capital <= 0:
            return 1, round_num, 0

        if np.random.rand() < win_prob:
            capital += 1
        else:
            capital -= 1

    return 0, max_rounds, capital

def run_monte_carlo(num_simulations, initial_capital, max_rounds, win_prob=18/37):
    ruin_indicator = np.empty(num_simulations, dtype=int)
    rounds_played = np.empty(num_simulations, dtype=int)
    final_capital = np.empty(num_simulations, dtype=int)

    for i in range(num_simulations):
        r, t, c = simulate_roulette_session(initial_capital, max_rounds, win_prob)
        ruin_indicator[i] = r
        rounds_played[i] = t
        final_capital[i] = c

    return ruin_indicator, rounds_played, final_capital
