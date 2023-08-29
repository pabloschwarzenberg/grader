def buscarTodas(a,b):
    palabra = list(a)
    i = 0
    resultado = []
    while i + len(b) <= len(a):
        k = ""
        for indice in range(len(b)):
            k += palabra[i+indice]
        if k == b:
            n=str(i)
            resultado.append(n)
        i += 1
    resultado = " ".join(resultado)
    return resultado

if __name__ == "__main__":
    palabra = input("¿Qué palabra deseas ingresar?:")
    abuscar = input("¿Qué palabra deseas buscar en la palabra anterior?:")
    print(buscarTodas(palabra,abuscar))
           