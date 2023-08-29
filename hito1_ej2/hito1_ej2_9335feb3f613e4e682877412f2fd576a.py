#Contestador de celular
numero = int(input("Ingrese su numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))


if hora>= 00 and hora<=7 :
        print("CONTESTAR")

elif numero%1000 == 909 and hora>7 and hora<=14:
    print("CONTESTAR")

elif numero != 909 and hora>7 and hora<=14:
        print("NO CONTESTAR")

elif numero//100000 == 877 and hora>=17 and hora<=19:
    print("NO CONTESTAR")
    
elif hora>19:
    print("NO CONTESTAR")
    