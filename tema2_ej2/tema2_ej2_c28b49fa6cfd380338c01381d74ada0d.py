# completa el código de la función
def amigos(x):
    suma=int(0)
    for k in range(1,int(x/2)+1):
        if((x%k)==0):
            suma=suma+k
    return suma

for i in range(2,100):
    ri=int(amigos(i))
    for j in range(i,100):
        rj=int(amigos(j))
        if((ri==j) and (rj==i)):
            print(str(i)+"\t"+str(j)+"\tson numeros amigos")
  
           