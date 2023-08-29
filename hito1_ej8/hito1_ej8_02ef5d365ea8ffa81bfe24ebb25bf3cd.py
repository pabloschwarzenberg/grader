num = input("Ingrese un número de hasta cuatro dígitos: ")

if len(num) == 4:
    m = num[-4]
    c = num[-3]
    d = num[-2]
    u = num[-1]
    print(m+'M +', c+'C +', d+'D +', u+'U')

elif len(num) == 3:
    c = num[-3]
    d = num[-2]
    u = num[-1]
    print(c+'C +', d+'D +', u+'U')

elif len(num) == 2:
    d = num[-2]
    u = num[-1]
    print(d+'D +', u+'U')

else:
    print(num+'U')