# Creating a tuple with integers
marks = (12,65,98,45,78,90)
print(marks)

# Creating a tuple with mixed data types
guess = (23, 'Lit', 2.33, 'River')
print(guess)

# Creating a tuple without parentheses
marks2 = 12, 65, 98, 45, 78, 90
print(marks2)
print(marks2[0])  # Accessing the first element

#nested tuple
nested_tuple = ('Luke', 2, (3, 4), [9,0,8])
print(nested_tuple)

# Accessing elements in a nested tuple
print(nested_tuple[2])  # Accessing the third element (which is a tuple)
print(nested_tuple[0][0])  # Accessing the first element of the nested tuple

# Slicing a tuple
letters = ('w','i','n','d','o','w')
print(letters[1:4])
print(letters[0:2])

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2

print(tuple3)

# Tuple methods

clothes =('shirt', 'pant', 'jacket', 'hat', 'shoes','shirt')
print(clothes.count('shirt'))
print(clothes.index('jacket'))

# Iterating through a tuple
for item in clothes:
    print('clothe is : ', item)