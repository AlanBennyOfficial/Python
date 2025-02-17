n, n1, n2, n3 = 0, 0, 1, 1

n = int(input("Enter the number of terms: "))
print("Fibonacci series:")

for _ in range(n):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
