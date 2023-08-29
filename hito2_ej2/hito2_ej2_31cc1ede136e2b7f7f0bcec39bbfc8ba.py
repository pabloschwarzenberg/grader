
def ordenados(cadena):
    n = len(cadena)
    cadena  = cadena.upper()
    validos = 'ACGT'
    pares   = 0

    # solo hasta penúltimo
    i = 0
    while not(i>=(n-1)): 
        elemento  = cadena[i]
        elemento2 = cadena[i+1]
        if (elemento<=elemento2):
            pares = pares + 1
        i = i + 1
        print(elemento)
        print(elemento2)
    # validar elementos en cadena
    noADN = 0
    i = 0
    while not(i>=n):
        elemento = cadena[i]
        if not(elemento in validos):
            noADN = noADN - 1
        i = i + 1

    # corrige de ser necesario
    if (noADN<0): 
        pares = noADN
        
    return(pares)

palabra=str(input("Ingrese la Cadena :"))
if (ordenados(palabra)) < 0:
    print("Secuencia Inválida")
else:
    print("Secuencia Correcta")