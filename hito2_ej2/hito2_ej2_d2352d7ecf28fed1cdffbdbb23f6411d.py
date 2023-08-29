def validar(secuencia):
    secuencia=secuencia.lower()
    secuencia=list(secuencia)
    a=secuencia.count("a")
    c=secuencia.count("c")
    t=secuencia.count("t")
    g=secuencia.count("g")
    suma=a+c+t+g
    if suma==len(secuencia):
        a="Secuencia Correcta"
    else:
        a="Secuencia Incorrecta"
    return a

secuencia=input()
print(validar(secuencia))