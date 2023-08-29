def adn(x):
    x = x.lower()
    i=0
    while i<len(x):
        if x[i]!='a' and x[i]!='c' and x[i]!='g' and x[i]!='t':
            return 'Secuencia incorrecta'
        else:
            i = i+1
    return 'Secuencia correcta'

secuencia = input('Escribe la secuencia de ADN: ')
print(adn(secuencia))