"""Lab 02.04 – Parentheses Matching"""

class ArrayStack:
    def __init__(self):
        self.data = list()
        self.size = 0

    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return
        else:
            self.size -= 1
            return self.data.pop()

    def is_empty(self):
        return self.size == 0

def is_parentheses_matching(equation):
    stack = ArrayStack()
    status = True

    for char in equation:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                status = False
            stack.pop()

    if not stack.is_empty():
        print(f"Parentheses in {equation} are unmatched")
        print("False")
        return

    if status == False:
        print(f"Parentheses in {equation} are unmatched")
        print("False")
        return

    print(f"Parentheses in {equation} are matched")
    print("True")

is_parentheses_matching(input())
