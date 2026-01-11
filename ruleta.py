import numpy as np
import matplotlib.pyplot as plt
from constante import TIPURI_PARIURI, NUMERE_ROSII, NUMERE_NEGRE, NUMERE_SNAKE

def get_winning_numbers(tip_pariu, numar_ales):

    if tip_pariu == "straight":
        return [numar_ales]
    
    elif tip_pariu in ["split", "street", "corner", "double_street", "basket", "first_four", "top_line"]:
        if tip_pariu == "basket" and numar_ales is None:
            return [0, 1, 2]
        if (tip_pariu == "first_four" or tip_pariu == "top_line") and numar_ales is None:
            return [0, 1, 2, 3]

        if isinstance(numar_ales, int):
            if tip_pariu == "street":
                return [numar_ales, numar_ales + 1, numar_ales + 2]
            if tip_pariu == "double_street":
                return [numar_ales + i for i in range(6)]

        if not isinstance(numar_ales, (list, tuple, np.ndarray)):
             raise ValueError(f"Pentru {tip_pariu}, trebuie specificată o listă de numere sau un număr de start valid.")
    
        nums = list(numar_ales)
        if tip_pariu == "split" and len(nums) != 2:
            raise ValueError("Pariul 'split' necesită exact 2 numere.")
        if tip_pariu == "street" and len(nums) != 3:
             raise ValueError("Pariul 'street' necesită exact 3 numere.")
        if tip_pariu == "corner" and len(nums) != 4:
             raise ValueError("Pariul 'corner' necesită exact 4 numere.")
        if tip_pariu == "double_street" and len(nums) != 6:
             raise ValueError("Pariul 'double_street' necesită exact 6 numere.")
        
        return nums

    elif tip_pariu == "red_black":
        if numar_ales in ["red", "roșu", "rosu"]: return NUMERE_ROSII
        if numar_ales in ["black", "negru"]: return NUMERE_NEGRE
        raise ValueError("Pentru 'red_black', alegeți 'roșu' sau 'negru'.")

    elif tip_pariu == "even_odd":
        if numar_ales in ["even", "par"]: return [i for i in range(1, 37) if i % 2 == 0]
        if numar_ales in ["odd", "impar"]: return [i for i in range(1, 37) if i % 2 != 0]
        raise ValueError("Pentru 'even_odd', alegeți 'par' sau 'impar'.")

    elif tip_pariu == "low_high":
        if numar_ales in ["low", "mic"]: return list(range(1, 19))
        if numar_ales in ["high", "mare"]: return list(range(19, 37))
        raise ValueError("Pentru 'low_high', alegeți 'mic' sau 'mare'.")

    elif tip_pariu == "dozen":
        if numar_ales == 1: return list(range(1, 13))
        if numar_ales == 2: return list(range(13, 25))
        if numar_ales == 3: return list(range(25, 37))
        raise ValueError("Pentru 'dozen', alegeți 1, 2 sau 3.")

    elif tip_pariu == "column":
        if numar_ales == 1: return list(range(1, 37, 3))
        if numar_ales == 2: return list(range(2, 37, 3))
        if numar_ales == 3: return list(range(3, 37, 3))
        raise ValueError("Pentru 'column', alegeți 1, 2 sau 3.")

    elif tip_pariu == "snake":
        return NUMERE_SNAKE
    
    else:
        raise ValueError(f"Tip pariu necunoscut sau neimplementat: {tip_pariu}")

def simulare_ruleta(nr_simulari, tip_pariu, numar_ales = None):
    if tip_pariu not in TIPURI_PARIURI:
        raise ValueError(f"Tip pariu invalid: {tip_pariu}. Opțiuni: {list(TIPURI_PARIURI.keys())}")

    cota = TIPURI_PARIURI[tip_pariu]
    
    winning_numbers = get_winning_numbers(tip_pariu, numar_ales)
    
    rezultate = np.random.randint(0, 37, size = nr_simulari)
    
    castiguri = np.where(np.isin(rezultate, winning_numbers), cota, -1)
    
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
    
    ylim_min = min(valoare_teoretica - 0.1, np.min(medii[100:]))
    ylim_max = max(valoare_teoretica + 0.1, np.max(medii[100:]))
    plt.ylim(ylim_min, ylim_max)

    plt.xlabel("Număr de simulări")
    plt.ylabel("Câștig mediu")
    plt.title(titlu)
    plt.legend()
    plt.show()

def main():
    nr_simulari = 1000000
    valoare_teoretica = - 1 / 37

    print("--- Simulare Ruletă ---")

    print("1. Pariu pe ROȘU")
    castiguri_rosu = simulare_ruleta(nr_simulari, "red_black", "roșu")
    print(f"   Câștig mediu estimat: {calculeaza_castig_mediu(castiguri_rosu):.5f}")
    plot_convergenta(castiguri_rosu, valoare_teoretica, "Convergența - Pariu pe Roșu")

    print("\n2. Pariu pe STRAIGHT (7)")
    castiguri_7 = simulare_ruleta(nr_simulari, "straight", 7)
    print(f"   Câștig mediu estimat: {calculeaza_castig_mediu(castiguri_7):.5f}")
    plot_convergenta(castiguri_7, valoare_teoretica, "Convergența - Pariu pe numărul 7")

    print("\n3. Pariu pe STREET (start 1 -> [1, 2, 3])")
    castiguri_street = simulare_ruleta(nr_simulari, "street", 1)
    print(f"   Câștig mediu estimat: {calculeaza_castig_mediu(castiguri_street):.5f}")
    
    print("\n4. Pariu pe SNAKE")
    castiguri_snake = simulare_ruleta(nr_simulari, "snake")
    print(f"   Câștig mediu estimat: {calculeaza_castig_mediu(castiguri_snake):.5f}")

    print("\n5. Pariu pe FIRST FOUR (0, 1, 2, 3)")
    castiguri_ff = simulare_ruleta(nr_simulari, "first_four")
    print(f"   Câștig mediu estimat: {calculeaza_castig_mediu(castiguri_ff):.5f}")

if __name__ == '__main__':
    main()
