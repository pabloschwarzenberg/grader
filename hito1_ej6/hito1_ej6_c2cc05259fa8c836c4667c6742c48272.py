#Ordenar tres números
numero1 = int(input("Ingrese el primer numero para ordenarlos de menor a mayor: "))
numero2 = int(input("Ingrese el segundo numero para ordenarlos de menor a mayor: "))
numero3 = int(input("Ingrese el tercer numero para ordenarlos de menor a mayor:"))

if numero1 <= numero2 and numero2 <= numero3:
    print(f"{numero1}, {numero2}, {numero3}")
elif numero3 <= numero1 and numero1 <= numero2:
    print(f"{numero3}, {numero1}, {numero2}")
elif numero2 <= numero3 and numero3 <= numero1:
    print(f"{numero2}, {numero3}, {numero1}")
elif numero1 <= numero3 and numero3 <= numero2:
    print(f"{numero1}, {numero3}, {numero2}")
elif numero2 <= numero1 and numero1 <= numero3:
    print(f"{numero2}, {numero1}, {numero3}")
elif numero3 <= numero2 and numero2 <= numero1:
    print(f"{numero3}, {numero2}, {numero1}")