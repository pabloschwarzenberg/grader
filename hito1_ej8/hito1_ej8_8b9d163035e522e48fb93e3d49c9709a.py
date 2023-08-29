n= int(input('Ingresar numero de 4 digitos: '))
m=int(n/1000)
c=int((n-m*1000)/100)
d=int((n-c*100-m*1000)/10)
u=int((n-m*1000-c*100-d*10))
if m!=0:
    print(m, 'M+', c, 'C+', d, 'D+', u, 'U')
elif m==0 and c!=0:
    print(c, 'C+', d, 'D+', u, 'U')
elif m==0 and c==0 and d!=0:
    print(d, 'D+', u, 'U')
elif m==0 and c==0 and d==0 and u!=0:
    print(u, 'U')      