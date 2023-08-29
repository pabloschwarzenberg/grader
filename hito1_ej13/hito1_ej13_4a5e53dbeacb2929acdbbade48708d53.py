def primear(a):
 for e in range(2,a):
  if(a%e==0):
   return False
 return True
lista=[]
def encontrar_factores(n):   
    for a in range(2,n):
        if(primear(a)==True and n%a==0):
            lista.append(a)            
            return encontrar_factores(int(n/a))
    lista.append(n)
n=int(input(""))
encontrar_factores(n)
print(lista)
    