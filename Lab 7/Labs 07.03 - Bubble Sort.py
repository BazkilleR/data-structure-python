"""Labs 07.03 - Bubble Sort"""
import json

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

            if arr[walker] < arr[walker - 1]:
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
