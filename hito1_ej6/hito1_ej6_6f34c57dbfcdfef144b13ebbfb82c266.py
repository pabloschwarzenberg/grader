#Ordenar tres números
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 <= num2 and num1 <= num3:
    mini_nu = num1
    if num2 <= num3:
        mi_nu = num2
        ma_nu = num3
    else:
        mi_nu = num3
        ma_nu = num2
elif num2 <= num1 and num2 <= num3:
    mini_nu = num2
    if num1 <= num3:
        mi_nu = num1
        ma_nu = num3
    else:
        mid_nu = num3
        max_nu = num1
else:
    mini_nu = num3
    if num1 <= num2:
        mi_nu = num1
        ma_nu = num2
    else:
        mi_nu = num2
        ma_nu = num1

print(mini_nu, ",", mi_nu, ",", ma_nu)