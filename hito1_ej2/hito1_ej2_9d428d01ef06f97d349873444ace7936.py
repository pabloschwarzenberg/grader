#Contestador de celular
a=int(input("Ingrese numero telefonico: "))
b=int(input("Ingrese hora de llamada "))
if 0<=b<=7:
    print("Resultado: CONTESTAR")
if 7<b<14:
    if (a%1000)==909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
if 14<=b<17:
    print("Resultado: CONTESTAR")
if 17<=b<=19:
    if (a//100000)==877:
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
if b>19:
    print("Resultado: NO CONTESTAR")