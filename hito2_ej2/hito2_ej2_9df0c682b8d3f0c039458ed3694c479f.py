def genoma(secuencia):
    d=secuencia.lower()
    b=["a","c","t","g"]
    for t in d:
        genoma=False
        if t!=b[0] and t!=b[1] and t!=b[2] and t!=b[3]:
                genoma=True
        else: genoma=False
    if genoma==False:
            print("secuencia correcta")
    elif genoma==True:
            print("secuencia incorrecta")
genoma(input())