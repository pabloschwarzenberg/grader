def mcm(a, b, ab):
    lista = [a, b]
    lista.sort()
    menor = lista[0]
    mayor = lista[1]
    resta = mayor - menor
    if resta == menor:
        return ab / menor
    else:
        return mcm(menor, resta, ab)
if __name__=="__main__":
    pass
           