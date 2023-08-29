#Ordenar tres números
num1 = input("Ingrese primer numero : ")
num2 = input("Ingrese segundo numero : ")
num3 = input("Ingrese tercer numero : ")
#condicional
if num1 <= num2 <= num3 :
    print(num1,",",num2,",",num3)
if num1 <= num3 <= num2 :
    print(num1,",",num3,",",num2)

if num2 <= num1 <= num3 :
    print(num2,",",num1,",",num3)
if num2 <= num3 <= num1 :
    print(num2,",",num3,",",num1)

if num3 <= num1 <= num2 :
    print(num3,",",num1,",",num2)
if num3 <= num2 <= num1 :
    print(num3,",",num2,",",num1)