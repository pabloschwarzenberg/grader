#Suma de los N primeros números
n = int(input("Ingrese un numero entero positivo: "))

if n > 0:
 for i in range(1,n):
     print (i)
     
else: 
     print("El numero ingresado es incorrecto. Intentelo nuevamente.")
     
suma = n*(n+1)/2
print(suma)