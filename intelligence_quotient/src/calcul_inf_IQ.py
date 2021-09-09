from math import sqrt, exp, pi
from typing import List

def calcul_IQ_inferior(myIQ: List[float]) -> None:
    x: int = 0
    probability_density: int = 0
    my_len: float = myIQ[len(myIQ) - 1]
    sigma: float = myIQ[1]
    mu: float = myIQ[0]

    while x < my_len:
        probability_density = probability_density + (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * pow((x - mu) / sigma, 2))
        x = x + 0.01

    print (f'{probability_density:0.1f}% of people have an IQ inferior to {myIQ[2]}')
