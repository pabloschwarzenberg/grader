def secuenciax(secuencia):
    for i in range(0,len(secuencia)+1):
        if secuencia[i]!="A" or secuencia[i]!="C" or secuencia[i]!="T" or secuencia[i]!="G" or secuencia[i]!="a" or secuencia[i]!="c" or secuencia[i]!="t" or secuencia[i]!="g":
            return "la secuencia " + secuencia + " es incorrecta"
        else:
            return "la secuencia " + secuencia + " es correcta"

secuencia=input()
w=secuenciax(secuencia)
print(w)
