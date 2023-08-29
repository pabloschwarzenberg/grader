#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora <= 7 :
    print("Resultado: CONTESTAR")
if hora < 14 and hora > 7 and numero % 1000 == 909 :
    print("Resultado: CONTESTAR")
if hora < 14 and hora > 7 and numero % 1000 != 909 :
    print("Resultado: NO CONTESTAR")
if hora > 14 and hora < 17:
    print("Resultado: NO CONTESTAR")
if hora >= 17 and hora <= 19 and numero > 87699999 and numero < 87800000 :
    print("Resultado: NO CONTESTAR")
if hora >= 17 and hora <= 19 and numero <= 87699999 and numero <= 87800000 :
    print("Resultado: CONTESTAR")
if hora > 19 and hora <= 23 :
    print("Resultado: NO CONTESTAR")            