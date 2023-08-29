# completa el código de la función
def suma_divisores(a):
    sumatoria = 0

    for i in range(1, a):
        if a % i == 0:
             sumatoria += i

    es_primo = True if sumatoria == 1 else False
    return (sumatoria, es_primo)
  
           