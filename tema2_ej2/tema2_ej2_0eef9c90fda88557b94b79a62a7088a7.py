# completa el código de la función
def amigos(a, b):
    lista = []
    lista2 = []
    sonamigos = False
    for i in range(1, a):
        
        divicion = a % i
        if divicion == 0:
            lista.append(i)
    for i in range(1, b):
        
        divicion = b % i
        if divicion == 0:
            lista2.append(i)
    SumaLista1 = sum(lista)
    SumaLista2 = sum(lista2)
    if SumaLista1 == b and SumaLista2 == a:
        sonamigos = True
    return sonamigos


