inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Finding the length of the inventory
inventory_len = len(inventory)

# Select first element in inventory
first = inventory[0]

# Select last element in inventory
last = inventory[-1]

# Select elements 2 through 6
inventory_2_6 = inventory[2:6]

# Select first three inventory elements
first_3 = inventory[:3]

# Count how many "twin bed" elements are there?
twin_beds = inventory.count("twin bed")

# Remove the fifth element in the list
removed_item = inventory.pop(4)

# Insert new item "19th Century Bed Frame" as 11th element
inventory.insert(10, "19th Century Bed Frame")

# Sort inventory variable
sorted_inventory = sorted(inventory)
inventory.sort()

# Printing commands
print(inventory)
print("")
print(inventory_len)
print("")
print(first)
print("")
print(last)
print("")
print(inventory_2_6)
print("")
print(first_3)
print("")
print(twin_beds)
print("")
print(sorted_inventory)
print("")