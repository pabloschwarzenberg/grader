secuencia=input('')
i=len(secuencia)-1
cont=0
while i>0:
    if secuencia[i]=='A' or secuencia[i]=='C' or secuencia[i]=='T' or secuencia[i]=='G':
        cont+=1
    i-=1
if cont==len(secuencia):
    print('secuencia correcta')
else:
    print('secuencia incorrecta')