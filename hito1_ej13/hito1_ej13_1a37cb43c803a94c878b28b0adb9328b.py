#Factores Primos
# Pedimos al usuario un número entero
numero = int(input())

# Variable para ir almacenando cada factor primo
factor_primo = 2

# Mientras el factor primo sea menor o igual que el número ingresado
while factor_primo <= numero:
    
    # Si el número es divisible entre el factor primo actual
    if numero % factor_primo == 0:
        # Imprimimos el factor primo
        print(factor_primo)
        # Dividimos el número entre el factor primo y actualizamos el contador
        numero //= factor_primo
        continue
    
    # Incrementamos el factor primo actual en 1
    factor_primo += 1
