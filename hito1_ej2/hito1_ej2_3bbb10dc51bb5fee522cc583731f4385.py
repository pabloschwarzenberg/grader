#Contestador de celular
numero = (input("Ingrese numero de 8 cifras: "))
hora = int(input("Ingrese la hora representada en el siguiente rango entre 0 y 23: "))
if(hora >= 0 and hora <= 7):
    print("CONTESTAR")
elif hora >= 8 and hora <=14 and int(numero[5:8]) == 909:
    print("CONTESTAR")
elif hora >= 17 and hora <=19 and int(numero[5:8]) == 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")        