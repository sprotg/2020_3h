def gcd1(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print(gcd1(1071, 462))

def gcd2(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(gcd2(1071, 462))

def gcd3(a,b):
    if b == 0:
        return a
    else:
        return gcd3(b, a % b)

print(gcd3(1071, 462))
