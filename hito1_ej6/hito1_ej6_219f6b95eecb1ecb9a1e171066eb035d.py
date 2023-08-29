#Ordenar tres números
num1 = eval(input("Ingrese primer número: "))
num2 = eval(input("Ingrese segundo número: "))
num3 = eval(input("Ingrese tercer número: "))
if num1<num2:
    if num1<num3:
        if num2<num3:
            print("El orden de menor a mayor es:", num1, ",", num2, ",", num3)
        else:
            print("El orden de menor a mayor es:", num1, ",", num3, ",", num2)
    else:
        print("El orden de menor a mayor es:", num3, ",", num1, ",", num2)
else:
    if num1<num3:
        print("El orden de menor a mayor es:", num2, ",", num1, ",", num3)
    else:
        if num2<num3:
            print("El orden de menor a mayor es:", num2, ",", num3, ",", num1)
        else:
            print("El orden de menor a mayor es:", num3, ",", num2, ",", num1)