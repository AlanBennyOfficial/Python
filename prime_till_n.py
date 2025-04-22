# Unobtimized

# def is_prime(num):
#   for x in range( 2, num):
#     if (num%x) == 0:
#       return False
#   return True

# lst = []

# x = int(input("Enter the number:"))

# for x in range( 0, x+1 ):
#     if( is_prime(x)):
#         lst.append(x)

# print(lst)


# With memoization
from functools import lru_cache
from time import perf_counter as pc

@lru_cache(maxsize=None) # cache the result indefinitely
def is_prime(num):
  for x in range( 2, num):
    if (num%x) == 0:
      return False
  return True

lst = []

x = int(input("Enter the number:"))

start = pc()

for x in range( 0, x+1 ):
    if( is_prime(x)):
        lst.append(x)

end = pc()

print(lst)
print(f"\nTime taken: {end - start} seconds")