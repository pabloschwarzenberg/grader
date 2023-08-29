#Descomponer un número
numero = int(input('Ingrese un numero a descomponer: '))

u = numero % 10
d = (numero // 10) % 10
c = (numero // 100) % 10
m = numero // 1000

if numero >= 1000:
    print (m, 'M + ',c, 'C +', d,'D +', u,'U')
elif numero >= 100:
    print (c, 'C +', d,'D +', u,'U')
elif numero >= 10:
    print (d,'D +', u,'U')
elif numero >= 1:
    print(u, 'U')