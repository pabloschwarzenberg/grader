#Contestador de celular
numero = int(input("Número: "))
hora = int(input("Hora: "))
if hora >=0 and hora <= 7:
    print("CONTESTAR")
elif numero%10**3 == 909 and hora >= 0 or hora <=14:
    print("CONTESTAR")
elif numero%10**3 != 909 and hora >= 0 or hora <=14:
    print("NO CONTESTAR")
elif numero%10**3 == 877 and hora >= 17 or hora <=19:
    print("NO CONTESTAR")
elif hora >= 17 or hora <=19:
    print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")  