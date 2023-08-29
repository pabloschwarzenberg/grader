def genoma(secuencia):

    permitidas = 'actg'

    for letra in secuencia:
        if letra.lower() not in permitidas:
            return 'secuencia incorrecta'
    
    return 'secuencia correcta'

print(genoma('actggctagfac'))      