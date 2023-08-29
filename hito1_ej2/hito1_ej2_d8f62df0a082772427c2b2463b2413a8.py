#Contestador de celular
listahora07 = [1,2,3,4,5,6,7]
listahora814 = [8,9,10,11,12,13,14]
listahora1519 = [17,19]
listahora2024 = [20,21,22,23,24]

numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
numero = str(numero)
hora = str(hora)

if hora in listahora07:
    print("CONTESTAR")
elif hora in listahora814:
    if numero[5] == "9" and numero[0] == "0" and numero[7] == "9" :
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora in listahora1519:
    if numero[0] == "8" and numero[1] == "7" and numero[2] == "7":
        print("NO CONTESTAR")
    elif numero[0:2] != "877":
        print("CONTESTAR")
elif hora in listahora2024:
    print("NO CONTESTAR")
