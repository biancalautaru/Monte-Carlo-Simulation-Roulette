import numpy as np
import matplotlib.pyplot as plt

def calculate_estimates(ruin_indicator, rounds_played, final_capital):
    return {
        "Ruin Probability": np.mean(ruin_indicator),
        "Average Time to Stop": np.mean(rounds_played),
        "Average Final Capital": np.mean(final_capital)
    }

def confidence_interval_clt(x):
    n = len(x)
    z = 1.96
    mean = np.mean(x)
    variance = np.var(x, ddof=1)

    error = z * np.sqrt(variance / n)

    return mean - error, mean + error

def plot_convergence_clt(x, title):
    n = len(x)
    averages = np.cumsum(x) / np.arange(1, n + 1)

    z = 1.96
    mean = np.mean(x)
    variance = np.var(x, ddof=1)

    k = np.arange(1, n + 1)
    error = z * np.sqrt(variance / k)

    plt.figure()
    plt.plot(averages, label=r"$\bar{S}_k$")
    plt.axhline(mean, color="red", linestyle="--", label=r"$\hat{\mu}$")

    plt.fill_between(k, mean - error, mean + error, color="red", alpha=0.2, label=r"$\pm z\sqrt{\sigma^2/k}$" )

    plt.xlabel("Number of Simulations (k)")
    plt.ylabel("Estimate")
    plt.title(title)
    plt.legend()
    # plt.show()