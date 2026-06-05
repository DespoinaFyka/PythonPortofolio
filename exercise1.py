# The initial list given
my_list = [2, 3, 5, 3, 7, 2, 5, 8, 5]

# I want to use something where I can store both value and its position, so I will use a dictionary
positions_list = {}

# Collect both the index and the value with enumerate function
# If it is the first time the value is found, a list is created for its positions
# Then the index is appended to the list each time the value is found
for i, value in enumerate(my_list):
    if value not in positions_list:
        positions_list[value] = []
    positions_list[value].append(i)

# Print the results as shown in the exercise
# I check if the length of the positions list is above 1, which means it is a duplicate value
for value, idxs in positions_list.items():
    if len(idxs) > 1:
        print(f"Duplicate value {value} found at positions: {idxs}")

# Why is this approach the best? 
# It scans the list only once and I get an O(n) time complexity
