

def secuencia(sec):
    correcta = 0
    genoma = ['a','c','t','g']
    for l in sec.lower():
        if not l in genoma:
            correcta += 1
    if correcta > 0:
        print('La secuencia ' + sec + ' es correcta')
    else:
        print('La secuencia ' + sec + ' es incorrecta')

# secuencias = ['actgacac', 'actgb', 'ACTG']
#
# for _ in secuencias:
#     secuencia(_)
