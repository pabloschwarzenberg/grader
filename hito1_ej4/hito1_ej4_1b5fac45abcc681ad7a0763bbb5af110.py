#Conversión de Decimal a Binario
print ("Decimal a Binario")
n=int(input("Ingrese un número: "))
b= ""
print("El número escogido es: ",n)
while n >0:
  resto= n % 2
  n = n // 2
  b = str(resto)+b
print("Resultado= ",b)