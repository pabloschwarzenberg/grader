#Contestador de celular
numtelf = int(input("Ingrese el número telefónico: "))
hora = int(input("Ingrese hora de llamada: "))

sobrante = numtelf%1000
sobrante2 = numtelf//100000

if hora >= 0 and hora<=6:
    print("CONTESTAR")
elif hora >= 7 and hora <=13:
    if sobrante == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >=14 and hora <=16:
    print("NO CONTESTAR")
elif hora >= 17 and hora <= 18:
    if sobrante2 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")    
elif hora>=19 and hora <=23:
    print("NO CONTESTAR")       