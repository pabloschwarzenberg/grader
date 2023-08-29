VARIABLE = int(input("Por favor ingresar numero de hasta cuatro cifras: "))
if 0 < VARIABLE < 10000:
 MILES = VARIABLE//1000
 CENTENAS = (VARIABLE%1000)//100
 DECENAS = ((VARIABLE%1000)%100)//10
 UNIDADES = ((VARIABLE%1000)%100)%10
 print(str(MILES)+"m + "+str(CENTENAS)+"c + "+str(DECENAS)+"d + "+str(UNIDADES)+"u")

else:
   print("Debe ser un número de hasta cuatro cifras")

