#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
numero2=str(numero)
a=numero2[5]+numero2[6]+numero2[7]
b=numero2[0]+numero2[1]+numero2[2]
if len(numero2)==8 and 0<=hora<=7:
    print("CONTESTAR")

elif len(numero2)==8 and hora<14 and a=="909":
    print("CONTESTAR")

elif len(numero2)==8 and 17<=hora<=19 and b!="877":
    print("CONTESTAR")

elif len(numero2)==8 and 19<hora<=23:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")

