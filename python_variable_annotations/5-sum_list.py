#!/usr/bin/env python3
""" Staticly typed list sum fucntion """

def sum_list(input_list: list[float]) -> float:
    """ Sums all float in a list """
    num: float = 0.0
    for i in input_list:
        num+=i
    return num
