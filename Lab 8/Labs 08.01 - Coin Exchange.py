"""Labs 08.01 - Coin Exchange"""

import json

def coinExchange(amount, coins):
    print("Amount: " + str(amount))

    tenBathAmount = min(amount // 10, coins.get(10))
    amount -= tenBathAmount * 10

    fiveBathAmount = min(amount // 5, coins.get(5))
    amount -= fiveBathAmount * 5

    twoBathAmount = min(amount // 2, coins.get(2))
    amount -= twoBathAmount * 2

    oneBathAmount = min(amount, coins.get(1))
    amount -= oneBathAmount

    coins_amount = tenBathAmount + fiveBathAmount + twoBathAmount + oneBathAmount

    if amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        print(f"  10 baht = {tenBathAmount} coins")
        print(f"  5 baht = {fiveBathAmount} coins")
        print(f"  2 baht = {twoBathAmount} coins")
        print(f"  1 baht = {oneBathAmount} coins")
        print("Number of coins: " + str(coins_amount))

def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    import json
    amount = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(amount, data)

main()