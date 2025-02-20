"""Labs 07.06 - Seats Number (Bubble Sorting)"""
import json

def juditem(item1: str, item2: str) -> bool:
    alpha1, num1 = item1[0], int(item1[1:])
    alpha2, num2 = item2[0], int(item2[1:])

    if alpha1 != alpha2:
        return alpha1 < alpha2
    else:
        return num1 < num2

def bubble_sort(arr, last_idx):
    """Sort data using bubble sort"""
    comparisons = 0
    current = 0
    sorted_status = False

    while current <= last_idx and sorted_status == False:
        walker = last_idx
        sorted_status = True

        while walker > current:
            comparisons += 1

            if juditem(arr[walker], arr[walker - 1]):
                sorted_status = False
                arr[walker], arr[walker - 1] = arr[walker - 1], arr[walker]
            walker -= 1
        current += 1

        print(arr)

    print(f"Comparison times: {comparisons}")

if __name__ == "__main__":
    arr = input()
    arr = json.loads(arr)
    last_idx = int(input())
    bubble_sort(arr, last_idx)
