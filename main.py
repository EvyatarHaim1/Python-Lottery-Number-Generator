import random

start = int(input("Start: "))
end = int(input("End: "))
amount = int(input("Amount Chosen: "))
if (amount <= 0):
    print("Amount chosen must be at least one!")
    quit()

if (end - start + 1 < amount):
    print("Amount chosen can't exceed avaliable numbers")
    quit()

numbers = random.sample(range(start, end + 1), amount)

print(numbers)
