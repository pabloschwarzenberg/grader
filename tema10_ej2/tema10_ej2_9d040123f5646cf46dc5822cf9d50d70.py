def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)
    Tabla = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        Tabla[i][0] = i
    for j in range(n + 1):
        Tabla[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                Tabla[i][j] = Tabla[i - 1][j - 1]
            else:
                Tabla[i][j] = 1 + min(Tabla[i - 1][j], Tabla[i][j - 1], Tabla[i - 1][j - 1])
                
    Numero = Tabla[-1][-1]
    if Numero > 1:
        Retorno = '+1'
    elif Numero == 1:
        Retorno = 'IB'
    elif Numero == 1:
        Retorno = '1S'
    elif Numero == 0:
        Retorno = '0D'
    print(Retorno)
if __name__=="__main__":
    palabra1= input('Ingrese la primera palabra: ')
    palabra2= input('Ingrese la segunda palabra: ')
    levenshtein(palabra1, palabra2)
           