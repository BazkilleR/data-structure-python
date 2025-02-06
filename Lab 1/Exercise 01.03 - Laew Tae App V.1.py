"""Laew Tae App V.1"""

class App:
    def __init__(self):
        self.random_count = 0
        self.menu_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]

    def random_food(self):
        self.random_count += 1

    def list_foods(self):
        self.menu_list.sort()
        print(self.menu_list)

menu1 = App()
menu1.list_foods()
