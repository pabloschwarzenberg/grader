# completa el código de la función
def suma_divisores(a):
    divisores = []
    indice = 0
    resultado = 0
    for i in range(1,a):
        if a % i ==0:
            divisores.append(i)
    while indice < len(divisores):
        resultado = resultado + divisores[indice]
        indice = indice + 1
    resultados = True
    for i in range(1,resultado):
        if resultado % i == 0:
            resultados = False
            print(resultado,",",resultados)
        else:
            print(resultado,",",resultados)
    if resultado == 1:
        print(resultado, ",", resultados)
    if resultado == 0:
        resultados = False
        print(resultado, ",", resultados)
    return resultado, resultados