# Swap 2 numbers with and without temp

a = int(input("First Number (a):"))
b = int(input("Second Number (b):"))

temp = a
a = b
b = temp

print("a = ", a)
print("b = ", b )

# Without temp

a = int(input("First Number (a):"))
b = int(input("Second Number (b):"))

a = a - b
a = a + b
b = a - b

print("a = ", a)
print("b = ", b )
