#find least common multiple of two numbers
x = int(input('What is your first number? '))
y = int(input('What is your second number? '))
a = 2
while a <= x * y:  #end of while loop isn't important, but that is the highest value that least common multiple could be so doesn't accidently run forever
    if a % x == 0 and a % y == 0:
        print (a)
        break
    else:
        a += 1
