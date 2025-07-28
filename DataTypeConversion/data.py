# Implicit type conversion

temp1 = 32
temp2 = 35.6
temp3 = temp1 + temp2

print(type(temp1))
print(type(temp2))
print(temp3)
print(type(temp3))

# Explicit type conversion
temp4 = '33'
temp6 = '30.8'
print(type(temp4))
print(type(temp6))

temp5 = int(temp4)
temp7 = float(temp6)

print(temp5)
print(temp7)
print(type(temp7))