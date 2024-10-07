#!/usr/bin/python3

import math
from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile

def find_best_xy(n):
    x = 1
    y = n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            x = i
            y = n // i
    return y, x

decompose = ParsedParameterFile(name="./system/decomposeParDict")
print(f"number of processors is {decompose['numberOfSubdomains']}")
best = find_best_xy(decompose["numberOfSubdomains"])
print(f"Setting number of processors configuration to {list((*best, 1))}")
decompose["coeffs"]["n"] = list((*best, 1))
decompose.writeFile()
