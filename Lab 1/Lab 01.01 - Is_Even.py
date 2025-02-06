"""Is_Even"""

def is_even(n):
    n = str(n)
    if n[-1] in ("0", "2", "4", "6", "8"):
        return True
    elif n[-1] in ("1", "3", "5", "7", "9"):
        return False

print(is_even(int(input())))
