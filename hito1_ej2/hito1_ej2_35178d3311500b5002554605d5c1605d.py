#Contestador de celular
#Contestadora automatica
numero = int(input("Ingrese un numero de telefono"))
hora = int(input("Ingrese una hora (entre las 0 y las 23"))
num_termina = numero%1000
num_empieza = numero//100000

if hora <= 7:
    print("CONTESTAR")
elif num_termina == 909:
    print("CONTESTAR")
elif hora>7 and hora<=14:
    print("NO CONTESTAR")
elif hora >= 17 and hora <19:
    print("CONTESTAR")
    if num_empieza == 877:
        print("NO CONTESTAR")
elif hora >= 19:
    print("NO CONTESTAR")     