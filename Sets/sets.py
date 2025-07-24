numbers = {1,2,3,4,5,6,7}
print(numbers)
numbers.add(9)
print(numbers)
numbers.discard(1)
print(numbers)

guesses = {9,'car', 0.78,(1,2,3)}
print(guesses)
print(type(guesses))
print(guesses.pop())
print(guesses)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))