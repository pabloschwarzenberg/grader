print("indique el numero a:")
a=int(input("a:"))
print("indique el numero b:")
b=int(input("b:"))
print("indique el numero c:")
c=int(input("c:"))
#proceso
if a<=b<=c:
    print("ordenar menor a mayor:",a,",",b,",",c)
elif a<=c<=b:
    print("ordenar menor a mayor :",a,",",c,",",b)
elif b<=a<=c:
    print("ordenar menor a mayor :",b,",",a,",",c)
elif b<=c<=a:
    print("el ordenar menor a mayor:" ,b,",",c,",",a)
elif c<=b<=a:
    print(" el orden a menor a mayor:",c,",",b,",",a)
elif c<=a<=b:
    print(" el orden a menor a mayor:",int(c),",",int(a),",",int(b))