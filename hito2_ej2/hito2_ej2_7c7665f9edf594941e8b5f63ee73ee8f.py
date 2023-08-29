def ADN(string):
    correcta = True
    for i in string:
        if i.lower() not in 'actg':
            correcta = False
    if not correcta:
        return 'Secuencia incorrecta'
    elif correcta:
        return 'Secuencia correcta'
x = input('Ingresar secuencia: ')
print(ADN(x))
