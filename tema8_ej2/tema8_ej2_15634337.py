__author__ = 'Domingo'
def buscarTodas(a,b):
    longitud=len(a)
    lista=[]
    for i in range(longitud):
        if a[i]==b:
            lista.append(str(i))
    solucion=' '.join(lista)
    return solucion
if __name__ == "__main__":
    print(buscarTodas('tres tristes tigres','t'))
    