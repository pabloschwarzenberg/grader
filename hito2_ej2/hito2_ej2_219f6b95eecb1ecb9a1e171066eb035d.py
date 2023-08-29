def secuencia_correcta(cadena):
    #es_ADN = False
    bases = ['A','C','G','T','a','c','g','t']
    c = 0
    for e in cadena:
        if e not in bases:
            #print(e)
            c += 1
    return c



if __name__ == "__main__":
    cad = input("Cadena:")
    resp = secuencia_correcta(cad)
    if resp == 0:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")