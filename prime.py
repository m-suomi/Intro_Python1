#check if number is prime or not
x = int(input('Please input your number: '))
a = x - 1
while a > 1:
    if x % a == 0:
        print(str(x) + ' is not a prime number.')
        break
    else:
        a -= 1
if a == 1:
    print(str(x) + ' is a prime number.')
