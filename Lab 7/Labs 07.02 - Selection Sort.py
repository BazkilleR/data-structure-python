"""Labs 07.02 - Selection Sort"""
import json

def selection_sort(arr, last_idx):
    """sort data with selection sort"""
    comparisons = 0
    count = min(len(arr), last_idx + 1)

    for i in range(count - 1):

        # find minimum
        min_idx = i
        for j in range(i + 1, count):
            comparisons += 1
            if arr[j] < arr[min_idx]:
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
