def es_primo(numero):
    i = 0
    cont = 2
    while numero > 0 and i <= numero:
        if numero%cont == 0:
            cont -= 1
            return False
        if numero == 1:
            return False
            
        else:
            return True
