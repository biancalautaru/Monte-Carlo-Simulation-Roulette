from monte_carlo import ruleaza_monte_carlo
from analiza import calculeaza_estimari, interval_incredere_tlc, plot_convergenta_tlc

def main():
    nr_simulari = 10000
    capital_initial = 100
    max_runde = 1000
    prob_castig = 18 / 37

    indicator_ruina, runde_pana_la_oprire, capital_final = ruleaza_monte_carlo(nr_simulari, capital_initial, max_runde, prob_castig)

    estimari = calculeaza_estimari(indicator_ruina, runde_pana_la_oprire, capital_final)
    print("Estimări Monte Carlo:")
    for k, v in estimari.items():
        print(f"  {k}: {v:.5f}")

    ic_ruina = interval_incredere_tlc(indicator_ruina)
    ic_timp = interval_incredere_tlc(runde_pana_la_oprire)
    ic_capital = interval_incredere_tlc(capital_final)
    print("\nIntervale de încredere 95%:")
    print(f"  P(ruină): [{ic_ruina[0]:.5f}, {ic_ruina[1]:.5f}]")
    print(f"  E[timp]: [{ic_timp[0]:.5f}, {ic_timp[1]:.5f}]")
    print(f"  E[capital]: [{ic_capital[0]:.5f}, {ic_capital[1]:.5f}]")

    plot_convergenta_tlc(indicator_ruina, "Convergența estimării P(ruină)")
    plot_convergenta_tlc(runde_pana_la_oprire, "Convergența estimării E[timp]")
    plot_convergenta_tlc(capital_final, "Convergența estimării E[capital]")

if __name__ == '__main__':
    main()
