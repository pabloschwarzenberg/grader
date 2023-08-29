n1=int(input("Ingrese Rut sin digito verificador: "))
mult=2
n2=0
n4=0
while n1 > 0:
    for i in range (mult):
        n2 = (n1 % 10)
        n1 = n1 // 10
        n3=n2*mult
        n4=n4+n3
        n3=0
        if mult==7:
            mult=2
        else:
            mult+=1
        if n1==0:
            break
n5=n4//11
n6=n4-(11*n5)
n7=11-n6

if n7==11:
    print("dv = 0")
elif n7==10:
    print("dv = K")
else:
    print("dv =", n7)