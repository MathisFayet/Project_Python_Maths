from typing import List
from math import pow

def chiSquare(my_list: List[float]) -> int:
    chi = 0
    for index in range(0, len(my_list[1])):
        chi += pow(my_list[1][index] - my_list[2][index], 2) / my_list[2][index]
    return (chi)