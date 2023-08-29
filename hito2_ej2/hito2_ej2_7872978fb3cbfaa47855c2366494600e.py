def geno(string):
    string.upper()
    genoma = ['A','C','T','G']
    eorr = 0

    for gtico in range(len(string)):
        if string[gtico] not in genoma:
            eorr+=1

    if eorr > 0:
        return 'secuencia incorrecta'

    else:
        return 'secuencia correcta'




gent = str(input("codigo genetico: "))
print(geno(gent))