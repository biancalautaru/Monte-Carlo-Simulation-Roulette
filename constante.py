import numpy as np

ASPECT_RULETA = np.array([0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26])

NUMERE_ROSII = np.array([1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36])
NUMERE_NEGRE = np.array([2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35])

NUMERE_SNAKE = np.array([1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34])

TIPURI_PARIURI = {
    "straight": 35,
    "split": 17,
    "street": 11,
    "corner": 8,
    "double_street": 5,
    "basket": 11,
    "first_four": 8,
    "top_line": 8,
    "dozen": 2,
    "column": 2,
    "even_odd": 1,
    "red_black": 1,
    "low_high": 1,
    "snake": 2
}
