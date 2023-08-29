#Ordenar tres números
n1=int(input(" Ingresa numero 1: "))
n2=int(input(" Ingresa numero 2: "))
n3=int(input(" Ingresa numero 3: "))

if n1 <= n2 and  n2 <= n3:
    print(n1,',',n2,',',n3)
if n1 <= n3 and n3 <= n2:
    print(n1,',',n3,',',n2)
if n2 <= n1 and n1 <= n3:
    print(n2,',', n1,',',n3)
if n2 <= n3 and n3 <= n1:
    print(n2,',',n3,',',n1)
if n3 <= n2 and n2 <=n1:
    print(n3,',',n2,',',n1)
if n3 <= n1 and n1 <= n2:
    print(n3,',', n1,',',n2)     