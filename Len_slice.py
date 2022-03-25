# Create a variable with all the named toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Create a variable with of prices that are related to the previous list of toppings
prices = [2, 6, 1, 3, 2, 7, 2]

# Find out how many slices are £2 each
num_two_dollar_slices = prices.count(2)

# Find length of number of toppings
num_pizzas = len(toppings)

# Print a message advertising our shop and the number of pizzas  we sell
print("we sell", num_pizzas, "different kinds of pizza!")

# Join the two prices and pizzas variables together
# index = -1
# while index < 6:
# index += 1
# print(index)
# pizza_and_prices = [toppings[index], prices[index]]

# Create a new 2D variable

pizzas_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# Sort pizzas_and_prices in ascending price value
pizzas_and_prices.sort(reverse=False)

# Select the first element to find the cheapest pizza slice
cheapest_slice = pizzas_and_prices[0]

# Select the last element to find the priciest pizza slice
priciest_pizza = pizzas_and_prices[-1]

# Remove anchovies since we just sold our last slice
pizzas_and_prices.pop()

# Add peppers pizza
pizzas_and_prices.insert(4, [2.5, "peppers"])

# Find the option of the cheapest three slices to offer to the mice
three_cheapest = pizzas_and_prices[:5]

# Printing commands
print("")
print(toppings)
print("")
print(prices)
print("")
print(num_two_dollar_slices)
print("")
print(num_pizzas)
print("")
print(pizzas_and_prices)
print("")
print(cheapest_slice)
print("")
print(priciest_pizza)
print("")
print(three_cheapest)

