#Descomponer un número
n = str(input("Ingrese un número de hasta 4 cifras: "))

if len(n)==4:
    M = n[0]
    C = n[1]
    D = n[2]
    U = n[3]
    print(M,'M +',C,'C +',D,'D +',U,'U')

elif len(n)==3:
    C = n[0]
    D = n[1]
    U = n[2]
    print(C, 'C +', D, 'D +', U, 'U')
elif len(n)==2:
    D = n[0]
    U = n[1]
    print(D, 'D +', U, 'U')
elif len(n)==1:
    U = n[0]
    print(U, 'U')
