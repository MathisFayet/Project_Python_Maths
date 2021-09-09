from typing import List

def printMyList2(my_list: List[float], index: int) -> None:
    checkValue: int = 0

    if (index == 1):
        print(f'  Ox\t', end="| ")
        for first in my_list[index]:
            checkValue = checkValue + first
            print(f'{first:0.0f}', end="\t| ")
        print(f'{checkValue:0.0f}')
    if (index == 2):
        print(f'  Tx\t', end="| ")
        for first in my_list[index]:
            checkValue = checkValue + first
            print(f'{first:0.1f}', end="\t| ")
        print(f'{checkValue:0.0f}')

def printMyList(my_list: List[float]) -> None:
    for index in range(len(my_list)):
        stock: int = 1
        if (index == 0):
            print(f'   x\t', end="| ")
            for first in my_list[index]:
                if (stock == len(my_list[index])):
                    second = first.split('-')
                    print(f'{second[0]}+', end="\t| ")
                else:
                    print(f'{first}', end="\t| ")
                stock = stock + 1
            print(f'Total')
        printMyList2(my_list, index)