# Check if the given number is prime or not
import sympy

n = int(input("Enter the number:"))

if (sympy.isprime(n)):
  print("It is prime")
else:
  print("It is not prime")
