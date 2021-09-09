from typing import List

from src.calculChiSquare import chiSquare
from src.calculMyFit import fitValidity
from src.fillMyList import fillMyList
from src.printMyList import printMyList

def my_dowels(my_list: List[float]) -> None:
    stock: int = 0
    for index in range(len(my_list)):
        stock += (index * my_list[index])
    stock = stock / 10000

    calculMyList = fillMyList(my_list, stock)
    printMyList(calculMyList)
    print(f'Distribution:\t\tB(100, {stock:0.4f})')

    calculMyChi = chiSquare(calculMyList)
    print(f'Chi-squared:\t\t{calculMyChi:0.3f}')

    calculMyDegrees = len(calculMyList[1]) - 2
    print(f'Degrees of freedom:\t{calculMyDegrees:0.0f}')

    calculMyFit = fitValidity(calculMyChi, calculMyDegrees)
    print(f'Fit validity:\t\t{calculMyFit}')