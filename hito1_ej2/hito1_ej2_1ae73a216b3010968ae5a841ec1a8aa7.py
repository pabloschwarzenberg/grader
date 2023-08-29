###Entrada
numC = str(input("Ingresa un número de celular: "))  # Numero telefonico de entrada
hora = int(input("Ingresa la hora a la que te están llamando: "))
if hora > 0 and hora < 7:
    print("CONTESTAR")
if hora > 8 and hora < 14 and str(numC[-3]) == "9" and str(numC[-2]) == "0" and str(numC[-1]) == "9":
        print("CONTESTAR")
else:
    if hora > 8 and hora < 14:
        print("NO CONTESTAR")
if hora >= 17 and hora < 19 and str(numC[0]) == "8" and str(numC[1]) == "7" and str(numC[2]) == "7":
    print("NO CONTESTAR")
else:
    if hora >= 17 and hora < 19:
        print("CONTESTAR")
if hora >= 19 and hora <=23:
    print("NO CONTESTAR")
if hora >=14 and hora < 16:
    print("NO CONTESTAR")
  