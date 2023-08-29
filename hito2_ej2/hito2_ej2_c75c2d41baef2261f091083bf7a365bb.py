g=input('Ingrese secuencia del genoma: ')
g=g.upper()
i=0
v=0
f=1
while i<len(g):
    if g[i]=='A' or g[i]=='C' or g[i]=='T' or g[i]=='G':
       v=v+1
    else:
        f=f-1
    i=i+1
if f<1:
    print('Secuencia incorrecta')
else:
    print('Secuencia correcta')

