"""Labs 05.03 - isIntersect(A, B, C)"""
import json

def main():
    a = json.loads(input())
    b = json.loads(input())
    c = json.loads(input())

    ans = False
    for i in a:
        if i in b and i in c:
            ans = True
            break
    print(ans)

main()