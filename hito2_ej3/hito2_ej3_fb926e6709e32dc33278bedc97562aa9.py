def subsecuencia(secuencia,n):
    secuencia=secuencia.upper()
    lista=[]

    for i in range(0,len(secuencia)-n+1):
        lista.append(secuencia[i:i+n])

    lista2=[]
    for j in lista:
        if lista.count(j)==1:
            lista2.append(j)
    if len(lista2)==0:
        print("ninguna")
    else:
        print(lista2)
        
f=input()
e=int(input())
subsecuencia(f,e)