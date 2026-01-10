import numpy as np

def simulare_sisune_ruleta(capital_initial, max_runde, prob_castig = 18 / 37):
    capital = capital_initial

    for runda in range(1, max_runde + 1):
        if capital <= 0:
            return 1, runda, 0

        if np.random.rand() < prob_castig:
            capital += 1
        else:
            capital -= 1

    return 0, max_runde, capital

def ruleaza_monte_carlo(nr_simulari, capital_initial, max_runde, prob_castig = 18 / 37):
    indicator_ruina = np.empty(nr_simulari, dtype = int)
    runde_pana_la_oprire = np.empty(nr_simulari, dtype = int)
    capital_final = np.empty(nr_simulari, dtype = int)

    for i in range(nr_simulari):
        r, t, c = simulare_sisune_ruleta(capital_initial, max_runde, prob_castig)
        indicator_ruina[i] = r
        runde_pana_la_oprire[i] = t
        capital_final[i] = c

    return indicator_ruina, runde_pana_la_oprire, capital_final