def longest_common_substring(str1, str2):
    """Lab 09.03 - Longest Common Substring (LCS)"""

    # Initialize DP table
    dp_table = [[0] * len(str2) for _ in range(len(str1))]

    # Track the maximum length and the last index of LCS in str2
    max_length = 0
    end_index = 0

    # Fill DP table
    for i, char1 in enumerate(str1):
        for j, char2 in enumerate(str2):
            if char1 == char2:
                if i > 0 and j > 0:
                    dp_table[i][j] = dp_table[i-1][j-1] + 1
                else:
                    dp_table[i][j] = 1

                # Update the maximum LCS length
                if dp_table[i][j] > max_length:
                    max_length = dp_table[i][j]
                    end_index = j  # Track the end index of LCS in str2

    # Extract the LCS substring
    if max_length > 0:
        longest_substring = str2[end_index - max_length + 1:end_index + 1]
        print(longest_substring)
        print(max_length)
    else:
        print("No common substring.")

# Read input strings
input_str1 = input()
input_str2 = input()

# Execute the function
longest_common_substring(input_str1, input_str2)
