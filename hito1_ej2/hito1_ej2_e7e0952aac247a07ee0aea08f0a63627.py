#Contestador de celular
#Contestador de celular
n = int(input("Ingrese numero de 8 cifras: "))
h = int(input("Ingrese hora de la llamada: "))

#Condicionales
if h == 0 or h == 1 or h == 2 or h == 3 or h == 4 or h == 5 or h == 6 or h == 7:
    print("Contestar")
    
elif (h == 8 or h == 9 or h == 10 or h == 11 or h == 12 or h == 13) and (n%1000 == 909):
    print("Contestar")
    
elif (h == 17 or h == 18 or h == 19) and h > 87700000:
    print("Contestar")
else:
    print("No contestar")

      