import sys

a=input("Numero hasta 4 digitos: ")
if len(a)==4:
    b=a[0]+"M"
    c=a[1]+"C"
    d=a[2]+"D"
    f=a[3]+"U"
    print(a,"+", b,"+",c,"+",d,"+",f)
if len(a)==3:
    g=a[0]+"C"
    h=a[1]+"D"
    i=a[2]+"U"
    print(g,"+", h,"+", i)
if len(a)==2:
    j=a[0]+"D"
    k=a[1]+"U"
    print(j,"+", k)
if len(a)==1:
    l=a[0]+"U"
    print(l)
if len(a)>4:
    sys.exit(1)
