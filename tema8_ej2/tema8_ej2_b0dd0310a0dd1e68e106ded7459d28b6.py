def buscarTodas(a,b):
    cont = 0
    a = list(a)
    print(a)
    texto = ""
    for i in a:
        print(i)
        if i == b:
            texto = texto + str(cont) + " "
        cont= cont+1    
    return (texto.strip())



if __name__ == "__main__":
    pass
           