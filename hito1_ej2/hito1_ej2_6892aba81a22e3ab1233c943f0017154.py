#Contestador de celular
numero= int(input("Ingrese numero telefonico: "))
hora= int(input("Ingrese hora de la llamada: "))

CHE= numero%1000
CON= CHE//100
if (hora>=0 or hora<=7):
    print("CONTESTAR")

elif (hora==24) and (CHE == 909):
    print("CONTESTAR")

elif (hora>=17 or hora<=19)and (CON == 877):
    print("NO CONTESTAR")

elif (hora>19):
    print("NO CONTESTAR")  