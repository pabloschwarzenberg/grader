def buscarTodas(a,b):
    lista = ""
    for i in range(len(a)):
        if(a[i]==b):
            lista += str(i)
            lista += " "
    lista = lista[:-1]
    if(len(lista)==0):
        return "no existe"    
    return lista
if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))
