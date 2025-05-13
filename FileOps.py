# with open("FileOps.txt", "w") as file:
#     file.write("This is a test file.\n")
#     file.write("It contains some sample text.\n")
#     file.write("This is the third line of the file.\n")


# with open("FileOps.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

import pickle

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)