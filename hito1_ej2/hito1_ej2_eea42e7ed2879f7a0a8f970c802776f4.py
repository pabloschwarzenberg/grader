#Contestador de celular
num = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))

if  0 <= hora <=7 :
    print ("CONTESTAR")
elif  7 <= hora <= 14:
    if num%1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 <= hora <= 19:
    if num//100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
