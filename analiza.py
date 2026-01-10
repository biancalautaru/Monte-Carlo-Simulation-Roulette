import numpy as np
import matplotlib.pyplot as plt

def calculeaza_estimari(indicator_ruina, runde_pana_la_oprire, capital_final):
    return {
        "Probabilitate ruină": np.mean(indicator_ruina),
        "Timp mediu până la oprire": np.mean(runde_pana_la_oprire),
        "Capital mediu final": np.mean(capital_final)
    }

def interval_incredere_tlc(x):
    n = len(x)
    z = 1.96
    miu = np.mean(x)
    sigma2 = np.var(x, ddof = 1)

    eroare = z * np.sqrt(sigma2 / n)

    return miu - eroare, miu + eroare

def plot_convergenta_tlc(x, titlu):
    n = len(x)
    medii = np.cumsum(x) / np.arange(1, n + 1)

    z = 1.96
    miu = np.mean(x)
    sigma2 = np.var(x, ddof = 1)

    k = np.arange(1, n + 1)
    eroare = z * np.sqrt(sigma2 / k)

    plt.figure()
    plt.plot(medii, label = r"$\bar{S}_k$")
    plt.axhline(miu, color="red", linestyle="--", label=r"$\hat{\mu}$")

    plt.fill_between(k, miu - eroare, miu + eroare, color="red", alpha=0.2, label=r"$\pm z\sqrt{\sigma^2/k}$" )

    plt.xlabel("Număr simulări (k)")
    plt.ylabel("Estimare")
    plt.title(titlu)
    plt.legend()
    plt.show()