# Exam question

orders = [1000, 2000, 3000, 4000, 5000]

GST = lambda x : x + x*(18/100)

total = list(map(GST,orders))

print(f"Final List = {total}")