from math import sqrt, exp, pi
from typing import List

def calcul_IQ_between(myIQ: List[float], myIQ2: float) -> int:
    probability_density: int = 0
    mu: float = myIQ[0]
    sigma: List[float] = myIQ[1]
    my_len: float = myIQ[len(myIQ) - 1]

    if (myIQ[3] < myIQ[2]):
        exit(84)

    while myIQ2 < my_len:
        probability_density = probability_density + (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * pow((myIQ2 - mu) / sigma, 2))
        myIQ2 = myIQ2 + 0.01

    print (f'{probability_density:0.1f}% of people have an IQ between {myIQ[2]} and {myIQ[3]}')