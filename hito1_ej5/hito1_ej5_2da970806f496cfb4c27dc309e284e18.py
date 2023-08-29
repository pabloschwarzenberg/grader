n=input("Ingrese su rut sin puntos ni guion:")
N=int(n)

if 10000000<=N<=99999999:
    a=(int(n[7]))*2
    b=(int(n[6]))*3
    c=(int(n[5]))*4
    d=(int(n[4]))*5
    e=(int(n[3]))*6
    f=(int(n[2]))*7
    g=(int(n[1]))*2
    h=(int(n[0]))*3
    i=int(a+b+c+d+e+f+g+h)
    j=int(i%11)
    k=int(11-j)
    if k==10:
        print("dv=k")
    elif j==0:
        print("dv=",j)
    else:
        print("dv=",k)
elif 1000000<=N<=9999999:
    l=(int(n[6]))*2
    m=(int(n[5]))*3
    ñ=(int(n[4]))*4
    o=(int(n[3]))*5
    p=(int(n[2]))*6
    q=(int(n[1]))*7
    r=(int(n[0]))*2
    L=int(l+m+ñ+o+p+q+r)
    M=int(L%11)
    Ñ=int(11-M)
    if Ñ==10:
        print("dv=k")
    elif M==0:
        print("dv=",M)
    else:
        print("dv=",Ñ)