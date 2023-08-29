def mcd(a,b):
    factores_a = []
    factores_b = []
    for i in range(1,a+1):
        if a%i == 0:
            factores_a.append(i)
    for i in range(1,b+1):
        if b%i == 0:
            factores_b.append(i)
    lista = factores_a[::-1]
    for k in lista:
        if k in factores_b:
            return k
def mcm(a,b,ab):
    resultado = a*b/mcd(a,b)
    return resultado
if __name__=="__main__":
    pass
           