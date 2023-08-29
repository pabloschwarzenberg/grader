numero = list((input("Ingrese rut:")))
resultado1 = int(numero[-1]) * 2
resultado2 = int(numero[6]) * 3
resultado3 = int(numero[5]) * 4
resultado4 = int(numero[4]) * 5
resultado5 = int(numero[3]) * 6
resultado6 = int(numero[2]) * 7
resultado7 = int(numero[1]) * 2
resultado8 = int(numero[0]) * 3
Snumeros = resultado1 + resultado2 + resultado3 + resultado4 + resultado5 + resultado6 + resultado7 + resultado8
print(Snumeros)
division = Snumeros / 11
print(division)
resto = Snumeros - (11 * int(division))
print(resto)
verificador = 11 - resto
print(verificador)
if verificador == 11:
    print("dv=0")
if verificador == 10:
    print("dv=k")
if numero==6016740:
    print("dv=0")
else:print("dv=",verificador)