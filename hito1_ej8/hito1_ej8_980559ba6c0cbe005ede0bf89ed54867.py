#Descomponer un número
n = str(input('Ingrese un numero a descomponer: '))
p =[]

for i in n:
    i = int(i)
    p.append(i)

if len(p) == 1:
    U = p[0]
    print(U'U')
elif len(p) == 2:
    U = p[1]
    D = p[0]
    print(D,'D + ',U,'U')
elif len(p) == 3:
    U = p[2]
    D = p[1]
    C = p[0]
    print(C,'C +',D,'D + ',U,'U')
elif len(p) == 4:
    U = p[3]
    D = p[2]
    C = p[1]
    M = p[0]
    print(M,'M +',C,'C +',D,'D + ',U,'U')

