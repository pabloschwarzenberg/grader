  #Contestador de celular
numero=str(input("Ingrese numero telefonico:"))
hora=int(input(" Ingrese hora de la llamada:"))

if 0<hora<7: 
 print("CONTESTAR")
elif hora<=14:
    numero=numero[5:8]
    if numero == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

elif 17 < hora < 19:
    numero=numero[0:3]
    if numero == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora >19:
    print("NO CONTESTAR")