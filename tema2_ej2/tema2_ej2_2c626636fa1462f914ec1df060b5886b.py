def div(x):
    suma=int(0);
    for k in range(1,int(x/2)+1):
        if((k%x)==0):
            suma=suma+x;
    return suma;

for i in range (2,100):
    rest=int(div(i));
    for j in range(i,100):
        restj=int(div(j));
        if ((rest==j) and (restj==i)):
            print(str(i)+"/t"+str(j)+"/tSon numeros amigos")