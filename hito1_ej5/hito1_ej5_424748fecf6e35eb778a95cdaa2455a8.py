#Cálculo del dígito verificador de un rut
n=input('ingrese su rut sin digito verificador:')
n=int(n)
if n>=10000000:
    n=str(n)
    x=n[7]
    y=n[6]
    z=n[5]
    a=n[4]
    b=n[3]
    c=n[2]
    d=n[1]
    e=n[0]
    x=int(x)
    y=int(y)
    z=int(z)
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    e=int(e)
    x=x*2
    y=y*3
    z=z*4
    a=a*5
    b=b*6
    c=c*7
    d=d*2
    e=e*3
    R=x+y+z+a+b+c+d+e
    Q=int(R/11)
    W=R-(11*Q)
    T=11-W
    if T == 11:
      print ('dv= 0')
    elif T == 10:
      print ('dv=k')
    else:
      print('dv = ',T)
elif n<10000000:
    n=str(n)
    y=n[6]
    z=n[5]
    a=n[4]
    b=n[3]
    c=n[2]
    d=n[1]
    e=n[0]
    y=int(y)
    z=int(z)
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    e=int(e)
    y=y*2
    z=z*3
    a=a*4
    b=b*5
    c=c*6
    d=d*7
    e=e*2
    R=y+z+a+b+c+d+e
    Q=int(R/11)
    W=R-(11*Q)
    T=11-W
    if T == 11:
      print ('dv= 0')
    elif T == 10:
      print ('dv=k')
    else:
      print('dv = ',T)