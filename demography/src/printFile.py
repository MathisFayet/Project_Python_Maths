from sys import argv
from math import sqrt
from typing import List

def printRoot_Population(index : int, a : float , b: float, check: bool) -> None:
    stock: int = 1000000

    if (check == True):
        print("\tRoot-mean-square deviation: ", format(sqrt(index) / stock, ".2f"), sep="")
        print("\tPopulation in 2050: ", format((2050 * b + a) / stock, ".2f"), sep="")
    if (check == False):
        print("\tRoot-mean-square deviation: ", format(sqrt(index) / stock, ".2f"), sep="")
        print("\tPopulation in 2050: ", format(((2050 - a) / b / stock), ".2f"), sep="")

def printCountry(my_list: list) -> None:
    print(f'Country:', end=' ')

    for i in range(len(my_list)):
        if i != (len(my_list) - 1):
            print(f'{my_list[i][0]}', end=' ')
        else:
            print(f'{my_list[i][0]}', end='\n')