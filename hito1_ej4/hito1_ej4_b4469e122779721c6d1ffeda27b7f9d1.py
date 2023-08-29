#Conversión de Decimal a Binario
print("Conversor Decimal a Binario")
x = int(input("Ingrse un numero: "))
y = ''
#Ecuacion prara transformar el numero a Binario
while x // 2 != 0:
 y =str(x % 2) + y
 x = (x//2)
 #Resultado
y=str(1)+ y
print("Resultado =",y)