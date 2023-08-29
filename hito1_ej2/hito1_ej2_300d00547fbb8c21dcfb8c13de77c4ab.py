#Contestador de celular
numero=input("ingrese numero telefonico: ")
hora=int(input("ingrese hora de llamada: "))




if 0<=hora<=7:
    print("CONTESTAR")
 
if 7<=hora<=14:
    if int(numero[5:8])==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if 17<=hora<=18:
    if int(numero[0:3])==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if hora>19:
    print("NO CONTESTAR")