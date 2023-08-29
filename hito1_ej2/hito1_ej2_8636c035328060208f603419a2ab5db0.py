#Contestador de celular
 
print("Contestador Automatico")

#Definir variables y solicitar informacion

num = str(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora: '))
num_1 = num[0:3]
num_2 = num[5:8]

#Operaciones

if 0<= hora <=7 :
    print("CONTESTAR")
elif 7 < hora < 14:
    if num_2 == "909":
        print("CONTESTAR")

    else:
        print("NO CONTESTAR")
elif hora >17 and hora <19:
    if num_1 == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora >=19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")