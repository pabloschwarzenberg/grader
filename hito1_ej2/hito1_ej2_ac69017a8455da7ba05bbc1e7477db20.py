numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >0 and hora <= 7:
    print("Contestar")

elif hora >14:
    print("No contestar")

elif hora >=17 and hora <=19 :
    print("Contestar")

elif hora >= 19 and hora <=23:
    print("No contestar") 