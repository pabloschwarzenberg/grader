#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))

if numero//10000000 >= 1 and hora <= 7:
    print("CONTESTAR")
elif numero//10000000 >= 1 and 8 <= hora <= 13 and numero%1000==909:
    print("CONTESTAR")
elif numero//10000000 >= 1 and 17 <= hora <= 19:
    if numero//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")