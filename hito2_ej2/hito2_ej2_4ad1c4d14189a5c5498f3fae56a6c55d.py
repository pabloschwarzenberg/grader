print('** VALIDAR SECUENCIAS DE ADN **')
def val_secuencia(secuencia):  #la función recibe un string asGtt (ejemplo)
    secuencia = secuencia.upper()
    lista_gen = ['A','C','G','T']
    lista_sec = list(secuencia)
    for i in lista_sec:
        if i not in lista_gen:
            return 'secuencia incorrecta'
    return 'secuencia correcta'

secuencia = input('Ingrese la secuencia: ')
print(val_secuencia(secuencia))
            
            
