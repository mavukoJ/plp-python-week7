
# Week 7 Assignment - List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# Print each item with its number
print("My Shopping List Report")

number = 1
for item in items:
    print(str(number) + ". " + item)
    number += 1

# Count item names with more than four letters
count = 0

for item in items:
    if len(item) > 4:
        count += 1

print("Items with more than 4 letters:", count)

# Find the longest item name using a loop
longest = items[0]

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item name:", longest)
