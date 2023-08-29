#Contestador de celular
 
numero_telefonico = int(input(">>>> Ingrese número telefónico: "))
hora = int(input(">>>> Ingrese hora de llamada: "))

if hora > 0 and hora <= 7:
    print(">>>> Resultado: CONTESTAR")

elif hora > 7 and hora <= 14 and str(numero_telefonico).endswith("909"):
    print(">>>> Resultado: CONTESTAR")

elif hora > 7 and hora <= 14:
    print(">>>> Resultado: NO CONTESTAR")

elif hora >= 17 and hora <= 19 and str(numero_telefonico).startswith("877"):
    print(">>>> Resultado: NO CONTESTAR")
    
elif hora >= 17 and hora <= 19:
    print(">>>> Resultado: CONTESTAR")
    
elif hora > 19:
    print(">>>> Resultado: NO CONTESTAR")

else:
    print(">>>> Resultado: NO CONTESTAR")