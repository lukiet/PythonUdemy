import os
print(os.getcwd())
print(os.getcwdb())

#show contents of current directory
print(os.listdir())

# Create a new directory named 'Test'
os.mkdir('Test')

print(os.listdir())

# Rename the directory 'Test' to 'Newt'
os.rename('Test', 'Newt')
print(os.listdir())