#Descomponer un número
numero=eval(input("Ingrese un numero de hasta 4 digitos"))

umil = numero // 1000
tmp = numero % 1000

centenas = tmp // 100
tmp = tmp % 100

decenas = tmp // 10
unidades = tmp % 10
if (numero >= 0 and numero<10):
    print(unidades,"U")
if  (numero >=10 and numero<100):
    print(decenas,"D +",unidades,"U")
if numero >= 100 and numero < 1000:
    print(centenas,"C+",decenas,"D+",unidades,"U")
if numero >= 1000 and numero < 10000:
    print(umil,"M+",centenas,"C+",decenas,"D+",unidades,"U")      