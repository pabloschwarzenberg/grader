def buscarTodas(a,b):
    resultado = ''
    for i in range(len(a)):
        if a[i] == b:
            if resultado == '':
                resultado += str(i)
            else:
                resultado += ' ' + str(i)
    return resultado

if __name__ == "__main__":
    pass
           