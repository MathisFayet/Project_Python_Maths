from typing import List
from math import factorial

def calculFactorial(n: int, k: int) -> int:
    factorial1 = factorial(k)
    factorial2 = factorial(n)
    stockFactorial = factorial(k - n)
    factorial2 = factorial2 * stockFactorial

    return (factorial1 / factorial2)

def fillMyList(my_list: List[float], binomial: int):
    myListRes: list[List] = [[],[],[]]
    stock: int = 0

    for idx in range(len(my_list) - 1):
        myListRes[0].append(idx)
        myListRes[1].append(my_list[idx])
        result = 100 * calculFactorial(idx, 100) * pow(binomial, idx) * pow((1 - binomial), 100 - idx)
        myListRes[2].append(result)
        stock = stock + result
    myListRes[0].append(idx + 1)
    myListRes[1].append(my_list[idx + 1])
    myListRes[2].append(100 - stock)

    first = []
    second = []
    third = []

    fillMyList2(myListRes, first, second, third)
    fillMyList3(first, second, third)

    myListRes[0] = first
    myListRes[1] = second
    myListRes[2] = third

    return (myListRes)

def fillMyList2(myListRes: List[float], first: list, second: list, third: list) -> None:
    for index in range(len(myListRes[0])):
        if (index > 0 and index < (len(myListRes[0])-1)):
            if myListRes[1][index] < 10:
                if (myListRes[1][index - 1] < myListRes[1][index + 1]):
                    first.append(str(index - 1) + '-' + str(index))
                    sum = myListRes[1][index - 1] + myListRes[1][index]
                    second.append(sum)
                    sum = myListRes[2][index - 1] + myListRes[2][index]
                    third.append(sum)
                elif (myListRes[1][index - 1] > myListRes[1][index + 1]):
                    first.append(str(index ) + '-' + str(index + 1))
                    sum = myListRes[1][index + 1] + myListRes[1][index]
                    second.append(sum)
                    sum = myListRes[2][index + 1] + myListRes[2][index]
                    third.append(sum)
            else:
                first.append(str(index))
                second.append(myListRes[1][index])
                third.append(myListRes[2][index])
        else:
            first.append(str(index))
            second.append(myListRes[1][index])
            third.append(myListRes[2][index])

def fillMyList3(first: list, second: list, third: list):
    index = 0

    while index < (len(first)-1):
        stock = first[index].split('-')
        if (len(stock) > 1):
            if (first[index - 1] == stock[0]):
                first.pop(index - 1)
                second.pop(index - 1)
                third.pop(index - 1)
            elif (first[index + 1] == stock[1]):
                first.pop(index + 1)
                second.pop(index + 1)
                third.pop(index + 1)
        else:
            index = index + 1