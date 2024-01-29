"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X. 
If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. 
It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30
"""

# take input
# count through the number
# if module = 2, then add to sum

number = int(input())

sum = 0
for num in range(number+1):
    if num % 2 == 0:
        sum += num

print(sum)