# heights = [180, 124, 165, 173, 189, 169, 146]

inputs = input("Enter a bunch of heights or you're getting deported OMG!: ").split()
heights = []

for i in inputs:
    heights.append(float(i)) 

print(heights)


total = 0
for height in heights:
    total += height

average = total/len(heights)
print("The average is:", round(average))

