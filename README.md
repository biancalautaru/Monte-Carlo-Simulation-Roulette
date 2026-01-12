# Simulare Monte Carlo – Ruletă Europeană

În acest proiect, este utilizată metoda Monte Carlo pentru estimarea unor cantități de interes asociate jocului de ruletă europeană. Scopul principal este analiza comportamentului pe termen lung al unui jucător care pariază constant, cu accent pe:
- probabilitatea de ruină
- timpul mediu până la ruină
- capitalul final mediu

Structura proiectului este următoarea:
```text
.
├── constants.py    # parametrii globali ai simulării
├── roulette.py     # simularea unei runde de ruletă
├── strategies.py   # strategii de pariere
├── monte_carlo.py  # simularea sesiunilor de joc
├── analysis.py     # estimări statistice și grafice
└── main.py         # script principal de rulare
```

## Simularea unei runde de ruletă (`roulette.py`)

Fișierul `roulette.py` conține funcții care modelează rezultatul unei singure runde de ruletă. Rezultatul este generat aleator, în concordanță cu probabilitățile reale ale jocului, iar câștigul sau pierderea jucătorului sunt determinate în funcție de tipul pariului efectuat.
Acest modul este utilizat ca element de bază în simularea sesiunilor de joc.

## Strategii de pariere (`strategies.py`)

Fișierul `strategies.py` implementează diferite strategii de pariere, care stabilesc valoarea pariului la fiecare rundă în funcție de istoricul jocului. Printre strategiile implementate se numără:
- strategia cu pariu constant (*flat betting*)
- strategia *Martingale*
- strategia *Fibonacci*
Aceste strategii sunt utilizate pentru a compara comportamentul capitalului și riscul de ruină în funcție de metoda de pariere aleasă.

## Simularea unei sesiuni de joc (`monte_carlo.py`)

Fișierul `monte_carlo.py` conține funcția care simulează o sesiune completă de joc. O sesiune constă într-o succesiune de runde de ruletă, în care capitalul jucătorului este actualizat la fiecare pas, în funcție de rezultatul rundei și de strategia de pariere utilizată.
Simularea se oprește atunci când capitalul jucătorului ajunge la zero (ruină) sau este atins un număr maxim de runde prestabilit.
Pentru fiecare sesiune sunt returnate:
- un indicator de ruină
- numărul de runde jucate
- capitalul final al jucătorului

## Rularea simulărilor Monte Carlo (`monte_carlo.py`)

Tot în fișierul `monte_carlo.py`, este implementată funcția care rulează un număr mare de simulări independente ale sesiunii de joc. Pentru fiecare simulare sunt colectate:
- variabila indicator de ruină
- timpul până la oprirea jocului
- capitalul final
Rezultatele sunt stocate în structuri de tip `numpy.array` și sunt utilizate ulterior în analiza statistică.

## Analiza statistică și reprezentări grafice (`analysis.py`)

Fișierul `analysis.py` conține funcții pentru prelucrarea rezultatelor obținute prin simulare. Sunt calculate:
- estimatori Monte Carlo pentru probabilitatea de ruină, timpul mediu până la oprire și capitalul final mediu
- intervale de încredere de 95%, bazate pe *Teorema Limită Centrală*
- grafice de convergență ale estimărilor Monte Carlo
Graficele ilustrează evoluția mediei cumulative a estimărilor și evidențiază rata de convergență de ordinul \frac{1}{\sqrt{n}}.

## Scriptul principal(`main.py`)

Fișierul `main.py` coordonează rularea întregii simulări. Acesta:
- inițializează parametrii
- rulează simulările Monte Carlo pentru diferite strategii
- afișează rezultatele numerice
- generează graficele comparative

## Parametrii globali (`constants.py`)

Fișierul `constants.py` conține parametrii principali ai simulării, precum:
- capitalul inițial
- numărul maxim de runde
- numărul de simulări Monte Carlo
- probabilitatea de câștig la o rundă
Modificarea acestor valori permite explorarea diferitelor scenarii de joc.

## Utilizare

Pentru rularea simulării, parametrii pot fi ajustați în fișierul `constants.py`, după care scriptul principal se rulează cu:
```bash
python3 main.py
```
