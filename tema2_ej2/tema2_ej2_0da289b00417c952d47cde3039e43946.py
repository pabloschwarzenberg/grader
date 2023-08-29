def amigos(a,b):
    s = 0
    for n in range(1,a):
        if a%n == 0:
            s = s + n

    s2 = 0
    for m in range(1,b):
        if b%m == 0:
            s2 = s2 + m

    if s == b and s2 == a and a != b:
        return True
    else:
        return False
    return

a = 220
b = 281
x = amigos(a,b)
print(x)