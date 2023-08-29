# por favor escribe aquí tu función
def es_primo(numero):
    valorverdad = 0
    if numero == 1:
        valorverdad = 1
    for i in range(2, numero, 1):
        if numero % i == 0:
            valorverdad = 1
    
    if valorverdad == 0:
        return True
    else:
        return False