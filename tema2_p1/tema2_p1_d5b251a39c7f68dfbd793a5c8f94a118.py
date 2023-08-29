# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Determinar el valor de la variable "numero"
numero = 17

# Verificar si "numero" es primo utilizando la función "es_primo()"
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")
   