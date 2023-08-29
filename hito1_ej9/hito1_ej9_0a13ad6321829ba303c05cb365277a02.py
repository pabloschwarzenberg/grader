a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
e = int(input("E: "))
f = int(input("F: "))


if ((-a/b) == (-d/e)):
    if ((c/b) == (f/e)):
        print("Infinitas soluciones")
        exit()
    else:
        print("Sin soluciones")
        exit()

a1 = a * e
c1 = c * e
d1 = d * -b
f1 = f * -b

x = (c1 + f1) / (a1 + d1)
y = (c - (a * x)) / b

print("X = " + str(x) + "\nY = " + str(y))