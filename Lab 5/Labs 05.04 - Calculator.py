"""Labs 05.04 - Calculator"""
def count():
    num = int(input())
    total = 0
    for i in range(1 , num+1):
        total += len(str(i) + "+")
    print(total)

count()