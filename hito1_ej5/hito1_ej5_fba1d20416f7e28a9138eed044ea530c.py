#Cálculo del dígito verificador de un rut
r=int(input('Ingresa el rut: '))
n_d=len(str(r))
c1=1
d1=0
d2=0
to=0
while c1<=n_d:
    d1=((r%(10**c1))-d1)//(10**(c1-1))
    m=((c1+5)%6)+2
    d2=m*d1
    to+=d2
    c1+=1
x=to%11
xs=str(x)
re=11-x
res=str(re)
if res=='10':
    print('dv=k')
elif res=='11':
    print('dv=0')
else:
    print('dv='+res)