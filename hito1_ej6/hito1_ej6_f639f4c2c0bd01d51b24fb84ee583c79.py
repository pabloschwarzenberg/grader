#Ordenar tres números
n1=int(input("n1: "))
n2=int(input("n2: "))
n3=int(input("n3: "))
if n1>n2 and n1>n3:
    nmax=n1
    if n2>n3:
        nmid=n2
        nmin=n3
    else :
        nmid=n3
        nmin=n2
elif n2>n1 and n2>n3:
    nmax=n2
    if n1>n3:
        nmid=n1
        nmin=n3
    else :
        nmid=n3
        nmin=n1
elif n3>n2 and n3>n1:
    nmax=n3
    if n2>n1:
        nmid=n2
        nmin=n1
    else :
        nmid=n1
        nmin=n2
print(nmin,",",nmid,",",nmax)