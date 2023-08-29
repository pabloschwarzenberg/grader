#Nota final
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

no1 = float(input("Ingrese la primera nota: "))
no2 = float(input("Ingrese la segunda nota: "))
no3 = float(input("Ingrese la tercera nota: "))
no4 = float(input("Ingrese la cuarta nota: "))

promedio = (0.3*no1)+(0.3*no2)+(0.3*no3)+(0.1*no4)

clear()
print(promedio)