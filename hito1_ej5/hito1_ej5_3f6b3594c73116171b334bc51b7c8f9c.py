#Cálculo del dígito verificador de un rut
rut=list(input("rut: "))
rut.reverse()
if len(rut)<8:
    n1=int(rut[0])
    n2=int(rut[1])
    n3=int(rut[2])
    n4=int(rut[3])
    n5=int(rut[4])
    n6=int(rut[5])
    n7=int(rut[6])
    p1=2
    p2=3
    p3=4
    p4=5
    p5=6
    p6=7
    p7=2
    multi=(n1*p1)+(n2*p2)+(n3*p3)+(n4*p4)+(n5*p5)+(n6*p6)+(n7*p7)
elif len(rut)>7:
    n1=int(rut[0])
    n2=int(rut[1])
    n3=int(rut[2])
    n4=int(rut[3])
    n5=int(rut[4])
    n6=int(rut[5])
    n7=int(rut[6])
    n8=int(rut[7])
    p1=2
    p2=3
    p3=4
    p4=5
    p5=6
    p6=7
    p7=2
    p8=3
    multi=(n1*p1)+(n2*p2)+(n3*p3)+(n4*p4)+(n5*p5)+(n6*p6)+(n7*p7)+(p8*n8)
mod=multi%11
finn= mod- 11 
fin=finn*-1
if fin == 11:
    print("dv=0")
elif fin==10:
    print("dv=k")
else:
    print("dv=",fin)