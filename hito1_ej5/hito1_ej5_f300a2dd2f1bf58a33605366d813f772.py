#Cálculo del dígito verificador de un rut
n=int(input())
rut=[int( x) for x in str(n)]
rut.reverse()
serie=2
n=0
a=0
if len(rut)>7:
    for x in rut[0:-2]:
        n+=int(x)*serie
        serie+=1
    a+=rut[-1]*3+rut[-2]*2
elif len(rut)==7:
    for x in rut[0:-1]:
        n+=int(x)*serie
        serie+=1
    a+=rut[-1]*2
    
b=a+n
c=b//11
w=b-(11*c)
11-w
if 11-w==11:
    dv=0
elif 11-w==10:
    dv="k"
else:
    dv=11-w
print("dv="+str(dv))
