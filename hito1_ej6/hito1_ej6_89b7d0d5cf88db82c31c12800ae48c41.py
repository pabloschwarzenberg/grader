gato = 0
perro = 0
cerpiente = 0

gato = int(input("ingrese el primer numero: "))
perro = int(input("ingrese el segundo numero: "))
cerpiente = int(input("ingrese el tercer numero :"))
i = min(gato,perro,cerpiente)
n = max(gato,perro,cerpiente)
d = (gato + perro +cerpiente) - i - n
print((i,d,n))