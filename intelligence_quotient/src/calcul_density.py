from math import sqrt, exp, pi
from typing import List

def calcul_density_IQ(myIQ: List[float]) -> None:
    mu: float = myIQ[0]
    sigma: List[float] = myIQ[1]
    index: int = 0

    while (index < 201):
        stock = (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * pow((mu - index) / sigma, 2))
        print(f'{index} {stock:0.5f}')
        index += 1