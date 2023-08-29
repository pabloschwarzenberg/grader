def buscarTodas(a,b):
    lista=[]
    for z1 in range(len(a)):
        if a[z1]==b:
            lista.append(str(z1))
    return " ".join(lista)

if __name__ == "__main__":
    pass


           