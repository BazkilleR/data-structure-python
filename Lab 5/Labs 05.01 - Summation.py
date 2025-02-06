"""Labs 05.01 - Summation (แบบที่ 1)"""

def main():
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(main())