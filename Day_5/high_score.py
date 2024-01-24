#scores = [78, 65, 89, 86, 55, 91, 64, 89]

inputs = input("Enter your scores bro: ").split()
scores = list(map(int, inputs))
print(scores)


highest = 0
for score in scores:
    if score > highest:
        highest = score

print("The highest score in the class is:", highest)

