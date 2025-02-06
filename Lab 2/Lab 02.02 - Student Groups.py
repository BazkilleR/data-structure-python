"""Lab 02.02 - Student Groups"""

class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """Stack"""
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
        """pop"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return
        else:
            self.size -= 1
            return self.data.pop()

    def is_empty(self):
        """is_empty"""
        return self.size == 0
    
    def get_stack_top(self):
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return
        top = self.data.pop()
        self.data.append(top)
        return top
    
    def get_size(self):
        return self.size
    
    def print_stack(self):
        print(self.data)

    def clear(self):
        """Clear the stack."""
        self.data = list()
        self.size = 0

def copy_stack(stack1, stack2):
    stack2.clear()
    stack3 = ArrayStack()
    for item in stack1.data:
        stack3.push(item)

    for item in stack3.data:
        stack2.push(item)

def main():
    std_stack = ArrayStack()
    count_group = int(input())
    count_std = int(input())
    result = ""

    for _ in range(count_std):
        std_stack.push(input())

    for current_group in range(1, count_group + 1):
        result += f"Group {current_group}: "
        index = 0
        clone_stack = ArrayStack()
        copy_stack(std_stack, clone_stack)

        while not clone_stack.is_empty():
            if (index == 0) or (index % count_group == 0):
                item = clone_stack.pop()
                result += item

                if clone_stack.get_size() >= count_group:
                    result += ", "
            else:
                clone_stack.pop()
            index += 1

        if current_group != count_group:
            result += "\n"

        std_stack.pop()
    print(result)

main()