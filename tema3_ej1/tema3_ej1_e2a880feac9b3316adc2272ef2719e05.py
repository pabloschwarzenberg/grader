# completa el código de la función
num1 = 220
num2 = 284
#Sumar los divisores del primer numero
sumaDivNum1 = 0 # Acumula los divisores del primer numero
for i in range(1,num1): # range(1,num1) = [1,2,3,4,5,6,......119]
    if num1%i==0:
        #print(i)
        sumaDivNum1 = sumaDivNum1 + i
print("La suma de los divisores de", num1, "es:", sumaDivNum1)