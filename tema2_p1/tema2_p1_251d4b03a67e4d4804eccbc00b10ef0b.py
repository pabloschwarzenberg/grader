# por favor escribe aquí tu función
def es_primo(numero_primo):
    if numero_primo < 2:
        return False
    
    for numero in range(2,numero_primo):
        if numero_primo % numero == 0:
            return False
        return True           