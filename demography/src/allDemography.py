from csv import reader
from typing import List

from src.calculFit import Fit1
from src.calculFit import Fit2
from src.printFile import printCountry

def loadMyYears(my_list: list) -> list:
    stock: list = []
    two: int = 2

    for i in range(two, len(my_list)):
        stock.append(int(my_list[i]))

    return (stock)

def countryTotal(country: list) -> List[int]:
    my_list = [0] * 58

    for i in range(0, len(country), 1):
        for j in range(2, len(country[i]), 1):
            my_list[j - 2] += int(country[i][j])

    return (my_list)


def searchMyData(my_list: list, tab: List[str]) -> list:
    stock = []

    for i in tab:
        for k in my_list:
            if (i == k[0] or i == k[1]):
                stock.append(k)
    stock.sort()

    return (stock)

def csvLoader() -> list:
    filename = './207demography_data.csv'
    my_list: list = []

    with open(filename, 'r') as csv_file:
        r = reader(csv_file, delimiter=';')
        for i in r:
            my_list.append(i)

        return (my_list)

def allDemography(tab: List[str]) -> None:
    my_list = csvLoader()
    tab_of_data = searchMyData(my_list, tab)
    tchao = 0.9820
    printCountry(tab_of_data)

    stock_list = loadMyYears(my_list[0])
    country = countryTotal(tab_of_data)

    print("Fit1")
    index1 = Fit1(country, stock_list)
    print("Fit2")
    index2 = Fit2(country, stock_list)

    print(f'Correlation: {(index1 / index2):0.4f}')