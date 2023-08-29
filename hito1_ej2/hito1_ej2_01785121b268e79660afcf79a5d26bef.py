#Contestador de celular
numero = int( input("ingrese telefono :"))
hora   = int( input("ingrese hora :"))
if (hora > 0) and (hora < 7):
 print("contestar")
elif hora < 14 and (numero%1000)== 909:
 print("contestar")
elif hora < 14 and (numero%1000)!= 909:
 print("no contestar")
elif hora > 17 and hora < 19 and round(numero/100000)==877:
 print("contestar")
elif hora > 17 and hora < 19 and round(numero/100000)!= 877:
 print("no contestar")
elif hora > 19:
 print("no contestar") 