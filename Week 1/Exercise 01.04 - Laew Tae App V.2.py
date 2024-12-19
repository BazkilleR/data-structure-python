"""Laew Tae App V.2"""

class App:
    def __init__(self):
        self.random_count = 0
        self.menu_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]

    def random_food(self):
        self.random_count += 1

    def list_foods(self):
        self.menu_list.sort()
        print(self.menu_list)

    def add_food(self, name):
        self.menu_list.append(name)

menu1 = App()
for _ in range(int(input())):
    menu1.add_food(input())
menu1.list_foods()
