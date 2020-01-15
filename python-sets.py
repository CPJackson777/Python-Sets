# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add('Aventador')
showroom.add('Ghibli')
showroom.add('DBS Superleggera')
showroom.add('720s')
print(showroom)

# Print the length of your set.
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add('720s')

# Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)

# Using update(), add two more car models to your showroom with another set.
showroom.update({"Corvette", "Camry"})
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard('Camry')
print(showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {'taurus', 'accord', 'Ghibli', '720s', '4runner'}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
existInBoth = showroom.intersection(junkyard)
print(existInBoth)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroom = showroom.union(junkyard)
print(showroom) 

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
showroom.discard("4runner")
print(showroom)