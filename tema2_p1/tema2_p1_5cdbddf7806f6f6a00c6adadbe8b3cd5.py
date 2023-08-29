def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

# Ejemplo de uso
numero = 17
resultado = es_primo(numero)

if resultado:
    print("Es primo")
else:
    print("No es primo")

 
           