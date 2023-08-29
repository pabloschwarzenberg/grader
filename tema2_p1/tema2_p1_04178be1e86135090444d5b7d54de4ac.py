#Escribe aqui tu funcion
def es_primo(num):
    if num <2:
        return False
    for k in range(2, num):
        if num %k ==0:
            return False
    return True
print (es_primo(3))