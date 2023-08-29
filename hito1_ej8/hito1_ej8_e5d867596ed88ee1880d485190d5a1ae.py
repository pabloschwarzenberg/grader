#ENTRADA
numero = int(input("Número natural de hasta 4 cifras: "))

#DESARROLLO
if 0<numero<9999:
  mil = numero//1000
  centena = (numero%1000)//100
  decena = ((numero%1000)%100)//10
  unidad = ((numero%1000)%100)%10

#SALIDA
  print(str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")
else:
  print("Debe ser un número de hasta 4 cifras")