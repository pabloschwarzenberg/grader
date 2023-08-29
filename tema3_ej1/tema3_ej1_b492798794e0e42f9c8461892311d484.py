# completa el código de la función
def suma_divisores(a):
    num1=int(input("Ingrese numero 1:"))
num2=int(input("Ingrese numero 2:"))
#Primer numero
sumaDivisorN1=0
for i in range(1,num1):
    if num1%i == 0:
        print(i)
        sumaDivisorN1 = sumaDivisorN1 + i
print("La suma de los divisores de", num1,"es:",sumaDivisorN1)

#Segundo numero
sumaDivisorN2=0
for i in range(1,num2):
    if num2%i == 0:
        print(i)
        sumaDivisorN2 = sumaDivisorN2 + i
print("La suma de los divisores de", num2,"es:",sumaDivisorN2)

if sumaDivisorN1 == num2 and sumaDivisorN2 == num1:
    print("Los numeros", num1,"y", num2,"Son numeros amigables")          
  return
           