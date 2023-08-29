r= str(input("Por favor ingrese su rut sin su dígito verificador (el número después del '-'): "))
f= int(r)
if 1000000 <= f <= 9999999:
       q=int(r[0]) * 2
       w=int(r[1]) * 7
       e=int(r[2]) * 6
       a=int(r[3]) * 5
       s=int(r[4]) * 4
       d=int(r[5]) * 3
       z=int(r[6]) * 2
       j=(q + w + e + a + s + d + z)
       k=(j % 11)
       l= 11-k
       if (l == 11):
           print("dv= ", 0)
       elif l ==10:
           print("dv= K")
       else:
           print("dv= ", l)
elif 10000000 <= f <=99999999:
    t=int(r[0]) * 3
    y=int(r[1]) * 2
    u=int(r[2]) * 7
    g=int(r[3]) * 6
    h=int(r[4]) * 5
    b=int(r[5]) * 4
    n=int(r[6]) * 3
    m=int(r[7]) * 2
    J= (t + y + u + g + h + b + n + m)
    K= (J % 11)
    L= 11-K
    if L == 11:
        print("dv= ", 0)
    elif L == 10:
        print("dv= k")
    else:
        print("dv= ", L)

else:
    print("El Rut no ha sido reconocido, por favor, vuelva a ingresarlo.")