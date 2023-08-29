# por favor escribe aquí tu función
numero=15
def es_primo(numero):
    contar=0
    for i in range(1,numero+1):
        if numero% i == 0:
            contar+=1
    if contar == 2:
        return True
    else:
        return False
print(es_primo(numero))