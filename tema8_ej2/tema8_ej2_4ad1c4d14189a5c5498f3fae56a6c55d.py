print('** BUSCAR TODAS **')
def buscarTodas(a,b):
    lista_frase = list(a)
    lista = []
    lista_s = []
    for i in range(len(lista_frase)):
        if lista_frase[i] == b:
            lista.append(i)
    for i in lista:
        lista_s.append(str(i)) 
    string = ' '.join(lista_s)
    return string
    

if __name__ == "__main__":
    a = input('Ingrese la frase o palabra: ')
    b = input('Ingrese la letra: ')
    print(buscarTodas(a,b))
           