#Entradas
numero = int(input("Ingresa un numero: "))

#Procedimiento

while numero > 0:
    resto = numero%2
    numero = numero//2

    
    print(resto,end="")