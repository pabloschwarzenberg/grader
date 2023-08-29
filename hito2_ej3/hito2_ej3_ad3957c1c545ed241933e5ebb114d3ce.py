lista = []
letras = input("Ingrese secuencia: ")
n = int(input("Numero: "))
lista = list(letras)
re = int(len(lista))

def validacion(re, n):
    if re % n == 0:
        resul = re / n
        print(resul)
    else:
        print("ninguna")

validacion(re,n)