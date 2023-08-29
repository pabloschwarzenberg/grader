#Contestador de celular
## ENTRADA DE DATOS - PROCESO - SALIDA DE DATOS

Número_Telefonico = int(input("Ingrese el Número Telefonico : "))
Hora_Llamada = int(input("Ingrese hora de la Llamada : "))

if Hora_Llamada == 0 or Hora_Llamada <=7:
    print("Resultado: CONTESTAR")
elif Hora_Llamada <14 or Número_Telefonico % 100 == 909:
    print("Resultado: CONTESTAR")
elif Hora_Llamada >= 17 and Hora_Llamada <= 19 and Número_Telefonico //10000000 == 877:
    print("Resultado: NO CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")     