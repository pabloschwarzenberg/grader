n=float(input())
n1=int(n)
lista=[]
#Transformar a binario
while (n1>=2):
  a=n1//2
  b=n1%2
  if (a>=2):
    n1=a
    lista.append(b)
    
  elif (a<2):
    lista.append(b)
    lista.append(a)
    break
#Invertir el binario
l = []
largo = len(lista)

contador = 0
while contador < largo:
    l.append(lista[largo-1-contador])
    contador = contador + 1


#Sacarlo de la lista para que sea un numero
u = largo - 1
e = 0
algo = 0

while e>=0:
    if e==largo:
        break
    f = (l[u-e]*10**e)
    algo = algo +f
    
    
    e=e+1
   
print ("resultado=",algo)