import math
numero = int(input("Introduce el número: "))
umil = (numero/1000)
tmp = (numero % 1000)
centenas = (tmp / 100)
tmp = (tmp % 100)
decenas = (tmp / 10)
unidades = (tmp % 10)
parte_decimal, parte_entera_m = math.modf(umil)
parte_decimal, parte_entera_c = math.modf(centenas)
parte_decimal, parte_entera_d = math.modf(decenas)
if parte_entera_m > 0:
 print (parte_entera_m,"M","+",parte_entera_c,"C","+",parte_entera_d,"D","+",unidades,"U")
if parte_entera_c > 0 and parte_entera_m : 0
print (parte_entera_c,"C","+",parte_entera_d,"D","+",unidades,"U")
if parte_entera_d > 0 and parte_entera_m :0
print (parte_entera_d,"D","+",unidades,"U")