def combinacion_numeros_binarios(n,a=""):
    if len(a)==n:
        print(a)
        return
    binarios=["0","1"]
    for i in binarios:
        a=a+i
        combinacion_numeros_binarios(n,a)
        a=a[:len(a)-1]
n=int(input())
combinacion_numeros_binarios(n)
           