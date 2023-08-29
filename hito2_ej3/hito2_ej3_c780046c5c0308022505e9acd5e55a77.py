secuencia=input('')
n=int(input(''))
i=len(secuencia)-1
cont=0
lista=[]
while i>0:
    trozo=secuencia[cont:n]
    if len(trozo)==3:
        lista.append(trozo)
    cont+=1
    n+=1
    i-=1
lista_anexa=lista
while lista_anexa!=[]:
    trozo=lista_anexa.pop(0)
    for x in lista:
        if trozo==x:
            lista.remove(trozo)
for c in lista:
    print(c)