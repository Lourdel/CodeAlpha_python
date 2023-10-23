#!/usr/bin/env python3

"""
Python program to find ranges of numbers with a difference of 2
from a given input range using a recursive approach.
"""


def range_of_2(start, end):
    """Finds ranges of numbers with a difference of 2 from a given range."""
    if end - start < 2:
        return []
    range_list = []

    for num in range(start, end - 1):
        if num + 2 <= end:
            range_list.append((num, num + 2))

    if not range_list:
        mid = (start + end) // 2
        left_range = range_of_2(start, mid)
        right_range = range_of_2(mid, end)
        return left_range + right_range

    return range_list


start = int(input('Enter start of the range: '))
end = int(input('Enter end of the range: '))

if start <= end:
    result = range_of_2(start, end)

    if result:
        print('Ranges with a difference of 2:')
        for res in result:
            print(res)
    else:
        print("No ranges with a diference of 2 found.")

else:
    print('Start should be less than or equal to the end')
