#solve  (a + (b - c) * d - e) * f = 75
#where each variable is a unique integer 1 to 6
#and be able to solve for answer equal to 22, 38, 46, 57, 75, 78, 80, 81, 88, 92, 100, 102, 104, 105

answer = int(input('Set the equation (a + (b - c) * d - e) * f equal to what value? '))

for a in range(1,7):
    for b in range (1,7):
        for c in range (1,7):
            for d in range (1,7):
                for e in range (1,7):
                    for f in range (1,7):
                        if a!=b and a!=c and a!=d and a!=e and a!=f and b!=c and b!=d and b!=e and b!=f and c!=d and c!=e and c!=f and d!=e and d!=f and e!=f:
                        #why doesn't something easier work like if a!=(b,c,d,e,f) and b!=(c,d,e,f)....
                            ans = (a + (b - c) * d - e) * f
                            if ans == answer:
                                print (a,b,c,d,e,f)
                                print(ans)
                                #more fancy output text with whole equation and each variable listed
                                #print('The answer to (a + (b - c) * d - e) * f = ' + str(answer) + ' is:')
                                #print('a='+str(a) + ' b='+str(b) + ' c='+str(c) + ' d='+str(d) + ' e='+str(e) + ' f='+str(f))
