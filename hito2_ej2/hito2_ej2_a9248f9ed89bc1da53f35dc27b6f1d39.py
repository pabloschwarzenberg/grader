a=input('ADN:')
a=a.upper()
len(a)
i=0
ver=0
fal=1
while i<len(a):
    if a[i]=='A' or a[i]=='C' or a[i]=='T' or a[i]=='G':
        ver=ver+1
    else:
        fal=fal-1
    i=i+1        
if fal<1:
    print('Secuencia incorrecta')
else:
    print('Secuencia Correcta')
