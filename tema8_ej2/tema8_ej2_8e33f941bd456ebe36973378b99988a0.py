a = 'tres tristes tigres'
b = 't'

def buscarTodas(a, b):
    x = []
    for i in range(len(a)):
        letra = a[i:i+1]
        if letra == b:
            x.append(str(i))
    resultado_formateado = ' '.join(x)
    return resultado_formateado

resultado = buscarTodas(a, b)