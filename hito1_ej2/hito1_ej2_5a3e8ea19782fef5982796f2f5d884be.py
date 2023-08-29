#Contestador de celular
numero=int(input("Ingrese número teléfonico de 8 cifras "))
hora=int(input("Ingrese hora de llamada "))
if 0<=hora<=7:
    print("CONTESTAR")
if 7<hora<14 and numero%1000==909:
    print("CONTESTAR")
if 7<hora<14 and not numero%1000==909:
    print("NO CONTESTAR")
if 14<=hora<17:
    print("NO CONTESTAR")
if 17<=hora<=19 and numero//100000==877:
    print("NO CONTESTAR")
if 17<=hora<=19 and not numero//100000==877:
    print("CONTESTAR")
if 19 < hora :
    print("NO CONTESTAR")      