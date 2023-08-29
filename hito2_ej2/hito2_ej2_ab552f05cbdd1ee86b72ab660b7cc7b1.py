def genoma(secuencia):
    s=secuencia.lower()
    g=["a","c","t","g"]
    for i in s:
        genoma=False
        if s!=g[0] and s!=g[1] and s!=g[2] and s!=g[3]:
                genoma=True
        else: genoma=False
    if genoma==False:
            print("secuencia correcta")
    elif genoma==True:
            print("secuencia incorrecta")
genoma(input())