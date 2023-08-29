#Ordenar tres números
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

# Ordenar los números de menor a mayor
if num1 <= num2 and num1 <= num3:
    primer_num = num1
    if num2 <= num3:
        segundo_num = num2
        tercer_num = num3
    else:
        segundo_num = num3
        tercer_num = num2
elif num2 <= num1 and num2 <= num3:
    primer_num = num2
    if num1 <= num3:
        segundo_num = num1
        tercer_num = num3
    else:
        segundo_num = num3
        tercer_num = num1
else:
    primer_num = num3
    if num1 <= num2:
        segundo_num = num1
        tercer_num = num2
    else:
        segundo_num = num2
        tercer_num = num1

# Imprimir los números ordenados
print(primer_num, segundo_num, tercer_num, sep=', ')
