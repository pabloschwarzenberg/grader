n=int(input("ingresa numero de 4 digitos: "))
d="D"
c="C"
m="M"
u="U"
p1=(n%10)
n1=str(p1)
n1=n1+"U"
n = n // 10

p2=(n%10)
n2=str(p2)
n2=n2+"D+"
n = n // 10

p3=(n%10)
n3=str(p3)
n3=n3+"C+"
n = n // 10

p4=(n%10)
n4=str(p4)
n4=n4+"M+"
n = n // 10

if p4>0:
    print(n4,n3,n2,n1)

elif p4==0 and p3>0:
    print(n3,n2,n1)

elif p4==0 and p3==0 and p2>0:
    print(n2,n1)

elif p4==0 and p3==0 and p2==0:
    print(n1)
