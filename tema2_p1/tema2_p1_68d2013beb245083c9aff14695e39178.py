# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    elif numero == 1:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True            
numero = 1
result = es_primo(numero)
if result is True:
    print(True)
else:
    print(False)
           