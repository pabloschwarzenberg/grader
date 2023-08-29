#Descomponer un número
numero = int(input("Numero natural de 1,2,3 o 4 cifras:"))
if 0<numero<10000:
 mil = numero // 1000
 centena = (numero%1000)//100
 decena = ((numero%1000%100)//10)
 unidad = ((numero%1000%100)%10)
 print(mil, "M+", centena, "C+", decena, "D+", unidad, "U")
else:
 print("Debe ser un numero de hasta 4 cifras:")

