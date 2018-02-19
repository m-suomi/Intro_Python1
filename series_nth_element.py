#for a series ao = 1, ai+1 = 2 * ai + 1 for i > 0
#find what the nth element in the series is
n = int(input('Which element do you want to find in the series? '))

a = 1
i = 0
while i < n:
    i += 1
    a = 2 * a + 1
    #print(i, a) #can print each iterative term and its value of the series up to requested term

#prints value with appropriate verbage for term 1st, 2nd, 3rd, or nth
if n == 1:
    print (str(n) + 'st element in the series = ' + str(a))
elif n == 2:
    print (str(n) + 'nd element in the series = ' + str(a))
elif n == 3:
    print (str(n) + 'rd element in the series = ' + str(a))
else:
    print (str(n) + 'th element in the series = ' + str(a))
