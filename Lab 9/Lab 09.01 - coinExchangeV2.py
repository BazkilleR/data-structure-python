import json

def merge_coin_combinations(current_combinations, previous_combinations):
    """Merge coin combinations while ensuring minimal coin usage."""
    merged_combinations = []
    for index, current_comb in enumerate(current_combinations):
        total_value = sum(coin * count for coin, count in current_comb.items())

        if total_value < index + 1:
            if previous_combinations[index - total_value]:
                current_comb.update(previous_combinations[index - total_value])

        merged_combinations.append(current_comb)
    return merged_combinations

def select_best_combination(option1, option2):
    """Selects the best combination of coins based on minimal count and optimal usage."""
    optimal_combinations = []
    for comb1, comb2 in zip(option1, option2):
        value1 = sum(coin * count for coin, count in comb1.items())
        value2 = sum(coin * count for coin, count in comb2.items())
        total_coins1 = sum(comb1.values())
        total_coins2 = sum(comb2.values())

        if value1 == value2:
            if total_coins1 < total_coins2:
                optimal_combinations.append(comb1)
            elif total_coins1 > total_coins2:
                optimal_combinations.append(comb2)
            else:
                if comb1 and comb2:
                    if list(comb2.items())[-1][-1] > list(comb1.items())[-1][-1]:
                        optimal_combinations.append(comb1)
                    else:
                        optimal_combinations.append(comb2)
                else:
                    if len(comb2) > len(comb1):
                        optimal_combinations.append(comb1)
                    else:
                        optimal_combinations.append(comb2)
        elif value1 > value2:
            optimal_combinations.append(comb1)
        else:
            optimal_combinations.append(comb2)

    return optimal_combinations

def coin_exchange(target_amount, available_coins):
    """Lab 09.01 - Coin Exchange Problem (Improved Version)."""

    # Initialize grid to store possible combinations
    dp_grid = []
    dp_grid.append([{}] * target_amount)  # Initial empty combination

    # Sort available coins in ascending order
    available_coins = {int(coin): count for coin, count in sorted(available_coins.items(), key=lambda x: int(x[0]))}

    # Process each coin type
    for coin_value, max_coin_count in available_coins.items():
        temp_combinations = []
        temp_combinations.append([{}] * target_amount)

        for coin_count in range(1, max_coin_count + 1):
            current_combinations = []
            for amount in range(1, target_amount + 1):
                if coin_count * coin_value <= amount:
                    current_combinations.append({coin_value: coin_count})
                else:
                    current_combinations.append({})

            current_combinations = merge_coin_combinations(current_combinations, dp_grid[-1])
            current_combinations = select_best_combination(temp_combinations[-1], current_combinations)
            temp_combinations.append(current_combinations)

        dp_grid.append(select_best_combination(dp_grid[-1], temp_combinations[-1]))

    # Retrieve final combination
    result_combination = dp_grid[-1][target_amount - 1]

    # Ensure all coin types are represented in the output
    for coin in available_coins:
        result_combination.setdefault(coin, 0)

    # Sort coins in descending order
    result_combination = {coin: count for coin, count in sorted(result_combination.items(), key=lambda x: -x[0])}

    # Calculate total amount achieved
    total_value = sum(coin * count for coin, count in result_combination.items())

    # Output the results
    print(f"Amount: {target_amount}")
    if total_value >= target_amount:
        print("Coin exchange result:")
        for coin, count in result_combination.items():
            print(f"  {coin} baht = {count} coins")
        print(f"Number of coins: {sum(result_combination.values())}")
    else:
        print("Can not exchange.")

# Read input values
target_amount = int(input())
available_coins = json.loads(input())

# Execute the coin exchange function
coin_exchange(target_amount, available_coins)
