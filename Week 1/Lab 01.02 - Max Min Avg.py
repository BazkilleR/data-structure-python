"""Max…Min…Avg"""
import json

def find_maax(data_list):
    maax = float("-inf")
    for num in data_list:
        if num > maax:
            maax = num
    return maax

def find_miin(data_list):
    miin = float("inf")
    for num in data_list:
        if num < miin:
            miin = num
    return miin

def find_avvg(data_list):
    count = len(data_list)
    total = 0

    for i in data_list:
        total += i

    avvg = round(total / count, 2)
    return avvg

def find_all(data_list):
    """Max…Min…Avg"""
    data_list = json.loads(data_list)
    maax = find_maax(data_list)
    miin = find_miin(data_list)
    avvg = find_avvg(data_list)
    return (maax, miin, avvg)

print(find_all(input()))
