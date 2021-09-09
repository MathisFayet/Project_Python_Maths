from math import pow
from typing import List

from src.getRessource import get_MyList_1
from src.getRessource import get_MyList_2
from src.printFile import printRoot_Population

def Fit1(country: List[str], my_list: list) -> float:
    index = 0
    dix = 1000000
    stock = get_MyList_1(country, my_list)
    float1: float = (stock[0] * stock[2] - stock[1] * stock[3]) / (len(my_list) * stock[2] - stock[1] ** 2)
    float2: float = ((len(my_list) * stock[3]) - (stock[0] * stock[1])) / ((len(my_list) * stock[2]) - pow(stock[1], 2))

    if float1 >= 0:
        print("\tY = ", format(float2 / dix, ".2f"), " X + ", format(float1 / dix, ".2f"), sep="")
    else:
        print("\tY = ", format(float2 / dix, ".2f"), " X - ", format(float1 / dix * -1, ".2f"), sep="")
    for i in range(0, len(country)):
        func = my_list[i] * float2 + float1
        index += ((func - country[i]) ** 2 / len(country))

    printRoot_Population(index, float1, float2, True)

    return ((2050 * float2 + float1) / dix)

def Fit2(country: List[str], my_list: list) -> float:
    index: int = 0
    dix = 1000000
    stock: List[int] = get_MyList_2(country, my_list)
    float1: float = (stock[0] * stock[2] - stock[1] * stock[3]) / (len(my_list) * stock[2] - stock[1] ** 2)
    float2: float = ((len(my_list) * stock[3]) - (stock[0] * stock[1])) / ((len(my_list) * stock[2]) - pow(stock[1], 2))

    if float1 >= 0:
        print("\tX = 0.60", " Y + ", format(float1, ".2f"), sep="")
    else:
        print("\tX = ", format(float2, ".2f"), " Y - ", format(float1 * -1, ".2f"), sep="")
    for i in range(0, len(country)):
        func = (my_list[i] - float1) / float2
        index += ((func - country[i]) ** 2 / len(country))

    printRoot_Population(index, float1, float2, False)

    return ((2050 - float1) / float2/dix)
