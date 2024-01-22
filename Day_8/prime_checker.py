
def prime_checker(number):
    if number < 4:
        return True
    for i in range(2,number-1):
        print(number, i)
        if number % i == 0:
            return False
    return True


n = int(input())
print(prime_checker(number = n))
