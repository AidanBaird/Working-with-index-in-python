owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

# Zip the two lists owners and dogs_names together
names_and_dog_names = zip(owners, dogs_names)

# Converting the zipped data back into a list
converted_names = list(names_and_dog_names)

# Printing commands
print(names_and_dog_names)
print("")
print(converted_names)