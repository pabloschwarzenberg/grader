def binario(n,soluciones = []):
    if len(soluciones)==n:
        print(soluciones)
    else:
        for i in range(2):
          binario(n,soluciones+[i])
n=int(input())
binario(n)










           