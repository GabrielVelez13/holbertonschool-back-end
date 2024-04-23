#!/usr/bin/env python3
""" Staticly typed mixed list sum fucntion """

def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    """ Sums a mixed list """
    num: float = 0
    for i in mxd_lst:
        num+=i
    return float(num)

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))