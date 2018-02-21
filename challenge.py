#solve  (a + (b - c) * d - e) * f = 75  where each variable is a unique integer 1 to 6

for a in range(1,7):
    for b in range (1,7):
        for c in range (1,7):
            for d in range (1,7):
                for e in range (1,7):
                    for f in range (1,7):
                        if a!=b and a!=c and a!=d and a!=e and a!=f and b!=c and b!=d and b!=e and b!=f and c!=d and c!=e and c!=f and d!=e and d!=f and e!=f:
                        #why doesn't something easier work like if a!=(b,c,d,e,f)
                            ans = (a + (b - c) * d - e) * f
                            if ans == 75:
                                print (a, b, c, d, e, f)
                                print (ans)

# instead of doing all the a!=, etc; this is another way to form that criteria if a not in (b,c,d,e,f) and b not in (c,d,e,f), etc.

#'a = ' + str(a) + 'b = ' + str(b) + 'c = ' + str(c)
