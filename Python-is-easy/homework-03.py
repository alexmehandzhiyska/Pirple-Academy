a = 5
b = "5"
c = -3


def find_equals(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a == b or a == c or b == c:
        return True
    else:
        return False


print(find_equals(a, b, c))
