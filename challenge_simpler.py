#solve  (a + (b - c) * d - e) * f = 75  where each variable is a unique integer 1 to 6

for a in range(1,4):
    for b in range (1,4):
        for c in range (1,4):
            if a != b and a != c and b != c:
            #why doesn't this work? if a != (b and c) and b != c:
                #print(a,b,c)
                ans = (a + (b - c))
                #print(ans)
                if ans == 4:
                    print (a, b, c)
                    print (ans)



#'a = ' + str(a) + 'b = ' + str(b) + 'c = ' + str(c)
