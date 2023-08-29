#Ordenar tres números
num1 = int(input("Ingrese un número entero ->"))   # menor a mayor
num2 = int(input("Ingrese un segundo número entero ->"))
num3 = int(input("Ingrese un tercer número entero ->"))

if num1 > num2 and num2 > num3:
                 print(num3, ",", num2, ",", num1) 
        
if num1 > num3 and num3 > num2:
    print(num2, ",", num3, ",", num1)
if num1 == num2 and num1 > num3:
    print(num3,",",num2,",",num1)

if num1 == num3 and num1 > num2:
    print(num2,",",num3,",",num1)
if num1 == num2 and num1 < num3:
    print(num1,",",num2,",",num3)
if num1 == num3 and num1 < num2:
    print(num1,",",num3,",",num2)

if num2 > num1 and num1 > num3:
    print(num3, ",", num1, ",", num2)
    
if num2 > num3 and num3 > num1:
    print(num1, ",", num3, ",", num2)
    
if num3 > num1 and num1 > num2:
    print(num2, ",", num1, ",", num3)
    
if num3 > num2 and num2 > num1:
    print(num1, ",", num2, ",", num3)