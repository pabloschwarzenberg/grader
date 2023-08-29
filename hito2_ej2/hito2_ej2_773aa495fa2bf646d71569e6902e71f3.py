# Validar Secuencias de ADN
# 3 points
#
# Escribe un programa que reciba como entrada un string y valide si esa secuencia podría
# representar una secuencia del genoma. El programa no debe distinguir entre mayúsculas
# y minúsculas. Si la secuencia podría representar un genoma (contiene solamente las letras A,C,T,G),
# tu programa debe imprimir el mensaje secuencia correcta. Si la secuencia no es válida tu
# programa debe imprimir el mensaje secuencia incorrecta.

# La secuencia actgacac es correcta
# La secuencia actgb es incorrecta
# La secuencia ACTG es correcta

def secuencia(sec):
    correcta = 0
    genoma = ['a','c','t','g']
    for l in sec.lower():
        if not l in genoma:
            correcta += 1
    if correcta > 0:
        print('La secuencia ' + sec + ' es incorrecta')
    else:
        print('La secuencia ' + sec + ' es correcta')

# secuencias = ['actgacac', 'actgb', 'ACTG']
#
# for _ in secuencias:
#     secuencia(_)