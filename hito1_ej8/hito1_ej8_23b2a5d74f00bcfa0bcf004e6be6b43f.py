#Descomponer un número
numero = int(input("Introduce el número: "))

umil = numero / 1000
tmp = numero % 1000
umil = int(umil)
centenas = tmp / 100
tmp = tmp % 100
centenas = int(centenas)
decenas = tmp / 10
decenas = int(decenas)
unidades = tmp % 10
unidades = int(unidades)

if len(str(numero)) < 2:
    print(unidades,"U")
elif len(str(numero)) < 3:
    print(decenas,"D +",unidades,"U")
elif len(str(numero)) < 4:
    print(centenas,"C +",decenas,"D +", unidades, "U")
elif len(str(numero)) < 5:
    print(umil, "M +", centenas, "C +",decenas, "D +", unidades, "U")