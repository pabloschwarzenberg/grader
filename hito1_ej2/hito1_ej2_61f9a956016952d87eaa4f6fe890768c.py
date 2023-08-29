#Contestador de celular
numeros=int(input("ingrese el numero de telefono:"))
hora=int(input("ingrese hora:"))

numero=str(numeros)
emer=numero[5:8]
spam=numero[0:3]
if len(numero)==8:
    if 0<=hora<=7:
        print("CONTESTAR")
    elif 8<=hora<=14 and emer=="909":
        print("CONTESTAR")
    elif 8<=hora<=14:
        print("NO CNONTESTAR")
    elif 17<=hora<=19 and spam=="877":
        print("NO CONTESTAR")
    elif 17<=hora<=19:
        print("CONTESTAR")   
    elif hora>19:
        print("NO CONTESTAR")

else:
    print("el numero no es de 8 cifras")      