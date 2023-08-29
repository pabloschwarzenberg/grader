#Contestador de celular
numero_tf = input("ingrese numero telefonico: ")
hora = int(input("ingrese la hora de llamada: "))

if 0<=hora<=7:
    print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")
elif numero_tf[5:8] == "909" and hora<14:
    print("CONTESTAR")
elif numero_tf[5:8] != "909" and hora<14:
    print("NO CONTESTAR")
elif numero_tf[0:3] == "877" and 17<=hora>=19:
    print("NO CONTESTAR")
elif numero_tf[0:3] != "877" and 17<=hora>=19:
    print("CONTESTAR")
else: 
    print("NO CONTESTAR")     