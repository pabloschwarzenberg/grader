def binario(x):
    a = ''
    while x // 2 != 0:
        a = str(x % 2) + a
        x = x // 2
    return str(x) + a
r = int(input('digite numero: '))
print("resultado=",binario(r))