"""Labs 07.04 - Seats Number (Insertion Sorting)"""
import json

def juditem(item1: str, item2: str) -> bool:
    alpha1, num1 = item1[0], int(item1[1:])
    alpha2, num2 = item2[0], int(item2[1:])

    if alpha1 != alpha2:
        return alpha1 < alpha2
    else:
        return num1 < num2

def insertion_sort(arr, last):
    """Sort data using insertion sort"""
    comparisons = 0
    count = min(len(arr), last + 1)

    for current in range(1, count):
        hold = arr[current]
        walker = current - 1

        while walker >= 0 and juditem(hold, arr[walker]):
            comparisons += 1
            arr[walker + 1] = arr[walker]
            walker -= 1

        if walker >= 0:
            comparisons += 1

        arr[walker + 1] = hold
        print(arr)

    print(f"Comparison times: {comparisons}")

if __name__ == "__main__":
    arr = input()
    arr = json.loads(arr)
    last = int(input())
    insertion_sort(arr, last)
