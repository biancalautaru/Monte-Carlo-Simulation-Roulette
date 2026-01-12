import bisect

fib_seq = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

def strategy_flat(last_win, last_bet):
    return 1

def strategy_martingale(last_win, last_bet):
    if last_win:
        return 1
    else:
        return last_bet * 2

def strategy_fibonacci(last_win, last_bet):
    try:
        current_idx = fib_seq.index(last_bet)
    except ValueError:
        idx = bisect.bisect_left(fib_seq, last_bet)
        if idx > 0 and fib_seq[idx-1] == last_bet:
             current_idx = idx - 1
        else:
             current_idx = 0

    if last_win:
        new_idx = max(0, current_idx - 2)
    else:
        new_idx = min(len(fib_seq) - 1, current_idx + 1)

    return fib_seq[new_idx]
