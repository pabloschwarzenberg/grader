def buscarTodas(a,b):
    k = 0
    u = ""
    for i in a:
        if i == b:
            u += str(k)+" "
        k += 1
    u = list(u)
    u.pop(-1)
    w = ""
    for i in u:
        w += i
    return w

if __name__=="__main__":
    palabra = "tres tristes tigres"
    letra = "t"
    buscador = buscarTodas(palabra,letra)
    print(buscador)