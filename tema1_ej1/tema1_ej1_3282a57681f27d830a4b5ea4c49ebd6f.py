#Suma de los N primeros números
def naturales(N):
  return N*(N+1)/2
dato=int(input("ingrese un nuñmero para generar la suma consecutiva de los numeros naturales hasta el numero ingresado: "))
print("la suma total de los numeros naturales consecutivos hasta el "+str(dato)+" es :"+str(naturales(dato))) 