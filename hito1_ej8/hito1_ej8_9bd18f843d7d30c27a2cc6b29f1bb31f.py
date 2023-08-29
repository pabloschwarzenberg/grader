#Descomponer un número
x = int(input())
y = str(x)
z = len(y)
if z == 4:
    m = y[0]
    c = y[1]
    d = y[2]
    u = y[3]
    print(m+'M','+', c+'C','+', d+'D','+', u+'U')
elif z == 3:
    c = y[0]
    d = y[1]
    u = y[2]
    print(c+'C','+', d+'D','+', u+'U')
elif z == 2:
    d = y[0]
    u = y[1]
    print(d+'D','+', u+'U')
elif z == 1:
    u = y[0]
    print(u+'U')