#Ordenar tres números
n1 = int(input("numero 1:"))
n2 = eval(input("numero 2:"))
n3 = eval(input("numero 3:"))

if n1 <= n2 and n1 <= n3:
    if n2 <= n3:
        print(n1,",",n2,",",n3)
    else: print(n1,",",n3,",",n2)
if n2 <= n1 and n2 <= n3:
    if n1 <= n3:
        print(n2,",",n1,",",n3)
    else: print(n2,",",n3,",",n1)
if n3 <= n1 and n3 <= n2:
    if n1 <= n2:
        print(n3,",",n1,",",n2)
    else: print(n3,",",n2,",",n1)