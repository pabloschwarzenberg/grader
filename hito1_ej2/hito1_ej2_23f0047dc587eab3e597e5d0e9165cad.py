#Contestador de celular
t=int(input("Ingrese numero telefonico:",))
h=int(input("Ingrese hora de la llamada:",))

if 0<=h<=7:
    print("CONTESTAR")
elif h<=14 and (t%1000)==909:
    print("CONTESTAR")
elif 17<=h<=19 and t//100000!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")