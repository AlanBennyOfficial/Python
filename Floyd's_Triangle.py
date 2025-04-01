def floyd_triangle(rows):
    number = 1
    for i in range(1, rows + 1):
        # Create a row list with i consecutive numbers starting at 'number'
        row = list(range(number, number + i))
        number += i
        # Use map to convert each number in the row to a string and join them with spaces.
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    rows = int(input("Enter the number of rows for Floyd's Triangle: "))
    floyd_triangle(rows)

