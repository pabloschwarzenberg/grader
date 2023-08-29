#Contestador de celular
numero=int(input("ingrese numero telefonico: "))
hora=int(input("ingrese hora de la llamada: "))

if 0 <= hora <= 7 :
    print("CONTESTAR")
elif 19 < hora < 0:
    print("NO CONTESTAR")

elif 8 <= hora < 14 and (numero-(numero-909)):
    print("CONTESTAR")

elif 5<= hora <=19 and numero==(numero-(numero-877)):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")      