numero = int(input("Número natural desde el numero 1,2,3 y 4 cifras: "))

if 0<numero<100000:

  MIL = numero//1000

  CENTENA = (numero%1000)//100

  DECENA = ((numero%1000)%100)//10

  UNIDAD = ((numero%1000)%100)%10

  print(str(MIL)+"M + "+str(CENTENA)+"C + "+str(DECENA)+"D + "+str(UNIDAD)+"U")

else:

  print("Debe ser un número de hasta 4 cifras, no mas")
