a1 = input("a1=")
a2 = input("a2=")
a3 = input("a3=")
if  a1<a2 and a2<a3:
    print(a1,",",a2,",",a3)
if a1<a3 and a3<a2:
    print(a1,",",a3,",",a2)
if a2<a1 and a1<a3:
    print(a2,",",a1,",",a3)
if a2<a3 and a3<a1:
    print(a2,",",a3,",",a1)
if a3<a1 and a1<a2:
    print(a3,",",a1,",",a2)
if a3<a2 and a2<a1:
    print(a3,",",a2,",",a1)
if a1==a3 and a3<a2:
    print(a1,",",a3,",",a2)
if a2==a3 and a3<a1:
    print(a2,a3,a1)
if a1==a2 and a1<a3:
    print(a1,",",a2,",",a3)
if a1<a3 and a3==a2:
    print(a1,",",a2,",",a3)
if a2<a3 and a1==a3:
    print(a2,",",a1,",",a3)
if a3<a1 and a1==a2:
    print(a3,",",a1,",",a2)

