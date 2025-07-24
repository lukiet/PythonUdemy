languages ={
    1: 'Python',
    2: 'Java',
    3: 'JavaScript',
    4: 'C++',
    5: 'Ruby',
    6: 'Go',
    7: 'Swift',
    8: 'Kotlin',
    9: 'PHP',
    10: 'Rust',
}

# Accessing dictionary elements
print(languages)
print(languages[2])
print(languages.get(5))

# Adding a new key-value pair
languages[11] = 'TypeScript'
print(languages)

# Removing a key-value pair
del languages[3]
print(languages)

print(languages.pop(6))
print(languages)
