n1=eval(input("ingrese primer numero :"))
n2=eval(input("ingrese segundo numero: "))
n3=eval(input(" ingrese tercer numero: "))
if n1<=n2<=n3:
    print(n1,",",n2,",",n3)
elif n2<=n1<=n3:
    print(n2,",",n1,",",n3)
elif n3<=n1<=n2:
    print(n3,",",n1,",",n2)
elif n3<=n2<=n1:
    print(n3,",",n2,",",n1)
elif n2<=n3<=n1:
    print(n2,",",n3,",",n1)
elif n1<=n3<=n2:
    print(n1,",",n3,",",n2)
