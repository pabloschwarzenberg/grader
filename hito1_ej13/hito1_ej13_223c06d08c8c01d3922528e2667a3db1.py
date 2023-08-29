def descomponer(numero):
    primos = []
    for i in range(2, numero+1):
        while numero % i == 0:
            primos.append(i)
            numero = numero / i
    return primos
numero = int(input("numero "))
resultado = descomponer(numero)
str1 = ''.join(str(e) for e in resultado)
print((str1)[0:1])
print((str1)[1:3])
print((str1)[3:5])