input = float(input('Input number please: '))
total = 0
while input >= 1:
    total += input
    print(input, total)
    input -= 1
print(total)
