fruits = ["Mango","Orange","Apple","Grape","Berry"]

print(fruits)
print(fruits[2])
print(len(fruits))

#adding a new item to array
fruits.append("Banana")
print(fruits)

#modifying elements
fruits[1] = "Guava"
print(fruits)

#removing an item from the array
cars = ["Toyota","Nissan","Mazda","Tesla","Honda","Mobius"]
print(cars)
del cars[1]
cars.remove("Tesla")
cars.pop(3)
print(cars)

#concatenating arrays
total = cars + fruits
print(total)

#slicing an array
print(total[1:4])
print(total[2:5])