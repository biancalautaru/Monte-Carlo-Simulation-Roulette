import numpy as np
import matplotlib.pyplot as plt

NUMERE_ROSII = np.array([1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36])
NUMERE_NEGRE = np.array([2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35])

def simulare_ruleta(nr_simulari, tip_pariu, numar_ales = None):
    rezultate = np.random.randint(0, 37, size = nr_simulari)

    if tip_pariu == "roșu":
        castiguri = np.where(np.isin(rezultate, NUMERE_ROSII), 1, -1)
    elif tip_pariu == "negru":
        castiguri = np.where(np.isin(rezultate, NUMERE_NEGRE), 1, -1)
    elif tip_pariu == "număr":
        if numar_ales is None:
            raise ValueError("Pentru pariu pe număr, trebuie specificat numar_ales")
        castiguri = np.where(rezultate == numar_ales, 35, -1)
    else:
        raise ValueError("Tip de pariu invalid")

    return castiguri

def calculeaza_castig_mediu(castiguri):
    return np.mean(castiguri)

def calculeaza_medie_cumulativa(castiguri):
    return np.cumsum(castiguri) / np.arange(1, len(castiguri) + 1)

def plot_convergenta(castiguri, valoare_teoretica, titlu):
    medii = calculeaza_medie_cumulativa(castiguri)

    plt.figure()
    plt.plot(medii, color = "blue", label = "Estimare Monte Carlo")
    plt.axhline(valoare_teoretica, linestyle = "--", color = "red", alpha = 0.5, label = "Valoare teoretică")

    plt.xlim(1, len(medii))
    plt.ylim(-0.1, 0.05)

    plt.xlabel("Număr de simulări")
    plt.ylabel("Câștig mediu")
    plt.title(titlu)
    plt.legend()
    plt.show()

def main():
    nr_simulari = 1000000
    valoare_teoretica = - 1 / 37

    # exemplul 1
    castiguri_rosu = simulare_ruleta(nr_simulari, "roșu")
    castig_mediu = calculeaza_castig_mediu(castiguri_rosu)
    print(f"Pariu pe roșu\n  Câștig mediu: {castig_mediu:.5f}\n")
    plot_convergenta(castiguri_rosu, valoare_teoretica, "Convergența Monte Carlo - Pariu pe roșu")

    # exemplul 2
    castiguri_7= simulare_ruleta(nr_simulari, "număr", 7)
    castig_mediu = calculeaza_castig_mediu(castiguri_7)
    print(f"Pariu pe numărul 7\n  Câștig mediu: {castig_mediu:.5f}\n")
    plot_convergenta(castiguri_7, valoare_teoretica, "Convergența Monte Carlo - Pariu pe numărul 7")

if __name__ == '__main__':
    main()