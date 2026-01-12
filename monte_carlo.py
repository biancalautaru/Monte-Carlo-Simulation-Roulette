import numpy as np
import strategies

def simulate_roulette_session(initial_capital, max_rounds, win_prob, strategy_func):
    capital = initial_capital
    round_num = 0
    
    current_bet = 1
    last_win = True
    
    while capital > 0 and round_num < max_rounds:
        round_num += 1
        
        suggestion = strategy_func(last_win, current_bet)
        current_bet = min(suggestion, capital)
        
        if np.random.rand() < win_prob:
            capital += current_bet
            last_win = True
        else:
            capital -= current_bet
            last_win = False
            
    is_ruined = 1 if capital == 0 else 0
    return is_ruined, round_num, capital

def run_monte_carlo(num_simulations, initial_capital, max_rounds=1000, win_prob=18/37, strategy_func=strategies.strategy_flat):
    ruin_indicator = np.empty(num_simulations, dtype=int)
    rounds_played = np.empty(num_simulations, dtype=int)
    final_capital = np.empty(num_simulations, dtype=int)

    for i in range(num_simulations):
        r, t, c = simulate_roulette_session(initial_capital, max_rounds, win_prob, strategy_func)
        ruin_indicator[i] = r
        rounds_played[i] = t
        final_capital[i] = c

    return ruin_indicator, rounds_played, final_capital
