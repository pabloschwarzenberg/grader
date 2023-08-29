def repite():
    i=0
    j=0
    k=entero
    while i<len(secuencia) and k<len(secuencia):
        t=secuencia[j:entero+j]
        u=secuencia[k:entero+k]
        if t==u:
            k+=entero
        if t!=u:
            print(u)
            print(t)
            j+=entero
            i+=entero
            
secuencia=input("")
entero=int(input(""))
repite()
      