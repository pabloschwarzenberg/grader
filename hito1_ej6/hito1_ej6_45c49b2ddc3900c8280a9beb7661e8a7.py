#Ordenar tres números
num1 = int(input("Digita un numero, cualquiera: "))
num2 = int(input("Digita un segundo numero, cualquiera: "))
num3 = int(input("Digita un tercer numero, cualquiera: "))
separacion = ","
if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1,separacion,num2,separacion,num3)
    else:
        print(num1,separacion,num3,separacion,num2)
if num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(num2,separacion,num1,separacion,num3)
    else:
        print(num2,separacion,num3,separacion,num1)
if num3 <= num1 and num3 <= num2:
    if num1 <= num2:
        print(num3,separacion,num1,separacion,num2)
    else:
        print(num3,separacion,num2,separacion,num1)