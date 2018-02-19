#find greatest common divisor (the greatest common factor) of two numbers
x = int(input('What is your first number? '))
y = int(input('What is your second number? '))
a = min(x, y)
while a > 0:  #the while end isn't important, just put > 0 so doesn't go forever
    if x % a == 0 and y % a == 0:
        print (a)
        break
    else:
        a -= 1
