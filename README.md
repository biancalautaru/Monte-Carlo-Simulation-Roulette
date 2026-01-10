# Simulare Monte Carlo – Ruletă Europeană

În acest proiect, este utilizată metoda Monte Carlo pentru estimarea unor cantități de interes asociate jocului de ruletă europeană. Scopul principal este analiza comportamentului pe termen lung al unui jucător care pariază constant, cu accent pe:
- probabilitatea de ruină
- timpul mediu până la ruină
- capitalul final mediu

## 1. Model matematic

## 2. Metoda Monte Carlo

Metoda Monte Carlo constă în simularea unui număr mare de traiectorii independente ale procesului descris mai sus și în estimarea mărimilor de interes prin medii empirice.

Estimatorii Monte Carlo sunt:
$$\hat{p} = \frac{1}{N} \sum_{i=1}^N I_i, \quad \widehat{E[T]} = \frac{1}{N} \sum_{i=1}^N T_i, \quad \widehat{E[C]} = \frac{1}{N} \sum_{i=1}^N C_i$$

## 3. Teorema Limită Centrală și analiza erorilor

Fie $(X_n)_{n \ge 1}$ variabile aleatoare independente și identic distribuite, cu $\mathrm{Var}(X_1) = \sigma^2 < \infty$.

Atunci, media empirică:
$$\overline{S_n} = \frac{1}{n} \sum_{i=1}^n X_i$$

converge în distribuție conform Teoremei Limită Centrale:
$$\overline{S_n} \xRightarrow{\text{D}} \mathcal{N}\left( \mu, \frac{\sigma^2}{n} \right)$$

Această proprietate permite construirea intervalelor de încredere de nivel $1 - \alpha$:
$$\mu \in \left[\overline{S_n} - z \sqrt{\frac{\sigma^2}{n}}, \overline{S_n} + z \sqrt{\frac{\sigma^2}{n}}\right]$$

## 4. Implementarea simulării

Structura proiectului este următoarea:
```text
.
├── ruleta.py        # simulare Monte Carlo simplă pentru o rundă
├── monte_carlo.py   # simularea sesiunilor de joc
├── analiza.py       # estimări statistice, intervale de încredere și grafice
└── simulare.py      # script principal de rulare
```

### 4.1. Simularea unei sesiuni de joc (`monte_carlo.py`)

Funcția `simuleaza_sesiune_ruleta` modelează evoluția capitalului unui jucător pe parcursul unei sesiuni de joc, presupunând un pariu constant de o unitate pe rundă. Capitalul este actualizat la fiecare pas în funcție de rezultatul aleator al ruletei.

Funcția returnează:
- un indicator de ruină ($1$ dacă jucătorul ajunge la capital nul înainte de $T$ sau $0$ altfel)
- numărul de runde jucate până la ruină sau până la oprire
- capitalul final

### 4.2. Rularea simulărilor Monte Carlo (`monte_carlo.py`)

Funcția `ruleaza_monte_carlo` repetă simularea unei sesiuni de joc de $N$ ori, considerând traiectorii independente ale procesului stochastic. Pentru fiecare simulare sunt colectate:
- variabila indicator de ruină
- timpul până la oprire
- capitalul final

Rezultatele sunt reprezentate în `np.array`-uri, care sunt utilizate ulterior în analiza statistică.

### 4.3. Estimări statistice, intervale de încredere și grafice (`analiza.py`)

Pe baza eșantionului obținut, funcția `calculeaza_estimari` determină estimatori Monte Carlo pentru cantitățile de interes, utilizând medii empirice.

Pentru analiza erorilor, funcția `interval_incredere_tlc` construiește intervale de încredere de 95%, folosind aproximația normală furnizată de Teorema Limită Centrală.

Funcția `plot_convergenta_tlc` reprezintă grafic evoluția mediei cumulative a estimării Monte Carlo. Sunt afișate:

- curba mediei cumulative $\overline{S_k}$
- o linie orizontală corespunzătoare estimării finale $\bar \mu$
- benzi de încredere de forma $\pm z\sqrt{\sigma^2/k}$, care evidențiază rata de convergență $\frac{1}{\sqrt k}$.

## 5. Utilizare

Parametrii principali (`N`, `C0`, `T`) pot fi modificați direct în fișierul `simulare.py`.

Rulare:

```bash
python3 simulare.py
```

## 6. Concluzii

## 7. Referințe bibliografice
