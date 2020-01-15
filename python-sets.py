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