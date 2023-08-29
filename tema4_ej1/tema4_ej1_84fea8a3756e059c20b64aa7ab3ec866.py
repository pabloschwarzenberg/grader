import random

def ocultar_letras(palabra,cantidad):
    contador = 0
    lista = list(palabra)
    vacia = []
    
    while contador != cantidad:
        aleatorio = random.randint(0,len(lista)-1)
        
        if aleatorio not in vacia:
            vacia.append(aleatorio)
        else:
            aleatorio = random.randint(0,len(lista)-1)
        lista[aleatorio] = '_'
        contador += 1
        
    lista = "".join(lista)
    return lista
    
def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
         