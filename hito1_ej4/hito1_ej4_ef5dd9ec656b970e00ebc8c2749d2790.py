print("convertir decimal")
numero=int(input("ingresa numero a convertir :"))
acumulacion =""
while numero > 0 :
    residuo = numero% 2
    numero = numero//2
    acumulacion =str(residuo) + acumulacion
print( "resultado= " +str(acumulacion))

