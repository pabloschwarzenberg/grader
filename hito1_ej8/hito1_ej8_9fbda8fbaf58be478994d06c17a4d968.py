#Descomponer un número
numero = int(input("Ingrese numero natural de 1,2,3 o 4 digitos: "))

if 0<numero<10000:

  M = numero//1000

  C = (numero%1000)//100

  D = ((numero%1000)%100)//10

  U = ((numero%1000)%100)%10

  print(str(M)+"M + "+str(C)+"C + "+str(D)+"D + "+str(U)+"U")

else:

  print("Debe ser un número de hasta 4 digitos")
