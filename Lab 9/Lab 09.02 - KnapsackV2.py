"""Lab 09.02 - KnapsackV2"""

import json

def knapsack(items, capacity):
    # Initialize DP table
    dp_grid = []

    for index, item in enumerate(items):
        item_id, item_value, item_weight = item  # Unpack item details
        current_row = []
        optimal_choices = []

        # Copy the previous row if available
        if dp_grid:
            previous_row = dp_grid[-1].copy()

        # Populate the current row based on item weight
        for weight in range(capacity):
            if item_weight <= weight + 1:
                current_row.append([item])
            else:
                current_row.append([])

        # Process and merge rows if it's not the first item
        if index:
            for weight_index, selected_items in enumerate(current_row):
                if selected_items:
                    total_weight = sum(i[2] for i in selected_items)
                    if total_weight < weight_index + 1:
                        if previous_row[weight_index - total_weight]:
                            selected_items += previous_row[weight_index - total_weight]

            # Compare with previous selections and choose the optimal one
            for prev_selection, new_selection in zip(previous_row, current_row):
                if prev_selection and new_selection:
                    prev_value = sum(i[1] for i in prev_selection)
                    new_value = sum(i[1] for i in new_selection)
                    if prev_value > new_value:
                        optimal_choices.append(prev_selection)
                    else:
                        optimal_choices.append(new_selection)
                elif prev_selection:
                    optimal_choices.append(prev_selection)
                elif new_selection:
                    optimal_choices.append(new_selection)
                else:
                    optimal_choices.append(prev_selection)

            dp_grid.append(optimal_choices)
        else:
            dp_grid.append(current_row)

    # Retrieve the final selected items
    selected_items = dp_grid[-1][-1]
    selected_items.sort(key=lambda x: x[0])  # Sort items based on their ID

    # Print results
    total_value = sum(item[1] for item in selected_items)
    print(f"Total: {total_value}")
    for item in selected_items:
        print(f"{item[0]} -> {item[2]} kg -> {item[1]} THB")

# Read input values
items_list = json.loads(input())  # List of items in the format: [[ID, Value, Weight], ...]
knapsack_capacity = int(input())

# Execute the knapsack function
knapsack(items_list, knapsack_capacity)
