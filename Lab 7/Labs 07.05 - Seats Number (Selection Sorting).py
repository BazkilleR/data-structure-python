"""Labs 07.05 - Seats Number (Selection Sorting)"""
import json

def juditem(item1: str, item2: str) -> bool:
    alpha1, num1 = item1[0], int(item1[1:])
    alpha2, num2 = item2[0], int(item2[1:])

    if alpha1 != alpha2:
        return alpha1 < alpha2
    else:
        return num1 < num2

def selection_sort(arr, last_idx):
    """sort data with selection sort"""
    comparisons = 0
    count = min(len(arr), last_idx + 1)

    for i in range(count - 1):

        # find minimum
        min_idx = i
        for j in range(i + 1, count):
            comparisons += 1
            if juditem(arr[j], arr[min_idx]):
                min_idx = j

        # swap position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(arr)

    print(f"Comparison times: {comparisons}")

if __name__ == "__main__":
    arr = input()
    arr = json.loads(arr)
    last = int(input())
    selection_sort(arr, last)
