def buscarTodas(a,b):
    final = ""
    p = 0
    for i in a:
        if i == b:
            final = final + str(p) + " "
        p = p + 1
    
        lista = list(final)
    del lista[-1]
    final2 = ""
    for i in lista:
        final2 = final2 + i

    return final2
    pass

if __name__ == "__main__":
    pass
           