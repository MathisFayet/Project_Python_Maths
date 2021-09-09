from math import pow, sqrt
from typing import List

def get_MyList_2(tab: List[str], my_list: list) -> List[int]:
    myList = [0, 0, 0, 0]

    for index in range(0, len(tab)):
        myList[0] += my_list[index]
        myList[1] += tab[index]
        myList[2] += pow(tab[index], 2)
        myList[3] += tab[index] * my_list[index]

    return (myList)

def get_MyList_1(tab: List[str], my_list: list) -> List[int]:
    myList = [0, 0, 0, 0]

    for index in range(0, len(tab), 1):
        myList[0] += tab[index]
        myList[1] += my_list[index]
        myList[2] += pow(my_list[index], 2)
        myList[3] += tab[index] * my_list[index]

    return (myList)