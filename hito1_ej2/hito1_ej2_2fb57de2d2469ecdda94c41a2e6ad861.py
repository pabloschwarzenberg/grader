#Contestador de celular
Numero=int(input("Ingrese numero telefonico: "))
Hora=int(input("Ingrese hora de llamada: "))
numero=str(Numero)
if 7>=Hora>=0:
    print("CONTESTAR")
elif 14>=Hora>=7 and numero[5:8]=="909":
    print("CONTESTAR")
elif 17<=Hora<=19 and numero[0:3]=="877":
    print ("NO CONTESTAR")
else:
    print("NO CONTESTAR")
