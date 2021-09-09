from typing import List

from src.calcul_density import calcul_density_IQ
from src.calcul_inf_IQ import calcul_IQ_inferior
from src.calcul_bet_IQ import calcul_IQ_between

def init_program(my_args: List[str]) -> None:
    if(my_args.simple != None):
        calcul_density_IQ(my_args.simple)
    elif (my_args.more != None):
        if (len(my_args.more) == 3):
            calcul_IQ_inferior(my_args.more)
        else:
            calcul_IQ_between(my_args.more, my_args.more[2])
    else:
        exit(84)