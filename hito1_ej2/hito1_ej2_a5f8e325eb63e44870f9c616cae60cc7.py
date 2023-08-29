#Contestador de celular
numero = str(input("ingrese numero telefoninico:"))
hora = int(input("ingrese hora de la llamada:"))

if 7 > hora > 0 or 17 > hora < 19:
  print("contestar")

if hora > 14 or 19 < hora <= 23:
   print("no contestar")

else:
    if hora > 14 and numero % 1000 == 909:
     print("contestar")
    if 17 > hora < 19 and str(numero[0:1]) == 8 and str(numero[1:2]) == 7 and str(numero[2:3]) == 7:
        print("no contestar")
    if 17 > hora < 19 and str(numero[0:1]) != 8 and str(numero[1:2]) != 7 and str(numero[2:3]) != 7:
        print("contestar")
