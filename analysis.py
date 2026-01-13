import numpy as np
import matplotlib.pyplot as plt

def compute_estimates(ruin_indicator, rounds_played, final_capital):
    return {
        "ruin_probability": np.mean(ruin_indicator),
        "average_time_to_stop": np.mean(rounds_played),
        "average_final_capital": np.mean(final_capital)
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

    plt.figure(figsize=(10, 6))
    plt.plot(averages, label=r"$\bar{S}_k$ (Estimate)")
    plt.axhline(mean, color="red", linestyle="--", label=r"$\hat{\mu}$ (Mean)")
    plt.fill_between(k, mean - error, mean + error, color="red", alpha=0.2, label="95% CI")

    plt.xlabel("Number of Simulations (k)")
    plt.ylabel("Estimate Value")
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    plt.close()
