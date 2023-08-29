def validar(secuencia):
    nucleotidos=['A','C','T','G']
    secuencia=list(secuencia.upper())
    for nucleotido in secuencia:
        if nucleotido not in nucleotidos:
            return 'secuencia incorrecta'
    return 'secuencia correcta'

seq=input("Ingrese una secuencia:\n")
print(validar(seq))