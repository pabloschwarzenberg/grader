#Soy Oscar Páez
def buscarTodas(a,b):
    lista = []
    for i in range(len(a)):
        if a[i]==b:
            lista.append(str(i))
        cadena = " ".join(lista)
    return cadena
if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))