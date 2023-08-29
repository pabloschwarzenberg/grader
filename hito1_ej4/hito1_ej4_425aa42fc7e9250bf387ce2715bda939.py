numeros=33
x=[]
while numeros >= 1:
    x.insert(0,numeros%2)
    numeros=numeros//2
binario="".join(str(i)for i in x)
print(binario)