"""Labs 07.01 - Insertion Sort"""
import json

def insertion_sort(arr, last):
    """Sort data using insertion sort"""
    comparisons = 0
    count = min(len(arr), last + 1)

    for current in range(1, count):
        hold = arr[current]
        walker = current - 1

        while walker >= 0 and hold < arr[walker]:
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
