"""Labs 08.02 - (2)Item Class"""

class Item:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

def knapsack(itemList, amount):
    itemList.sort(key=lambda x: x.get_price() / x.get_weight(), reverse=True)

    print(f"Knapsack Size: {amount} kg")
    print("===============================")

    total_weight = 0
    total_price = 0
    for item in itemList:
        total_weight += item.get_weight()

        if total_weight > amount:
            break

        total_price += item.get_price()
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")

    print(f"Total: {total_price} THB")

def main():
    import json
    items = []
    num_items = int(input())
    for _ in range(num_items):
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()