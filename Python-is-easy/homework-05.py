def solve():
    for i in range(1, 101):
        currentString = ''
        if i % 3 == 0:
            currentString += 'Fizz'
        if i % 5 == 0:
            currentString += 'Buzz'
        print(currentString) if currentString != '' else print(i)


solve()
