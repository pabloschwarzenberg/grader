#Conversión de Decimal a Binario
n=int(input("Ingrese un numero: "))
t=""
while n >= 2:
 t=t+str(round(n%2,0))
 n=n//2
 
t=t+str(n)
print("resultado = "+t[::-1])
     