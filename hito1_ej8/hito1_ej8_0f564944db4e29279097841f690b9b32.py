#Descomponer un número
n=int(input('Ingrese numero de 4 digitos:'))
n_falso=str(n)
if len(n_falso)>4:
    print('Ingresaste un numero que no cumple lo requerido')

elif len(n_falso)<=4:
    M=n//1000
    n=n%1000
    C=n//100
    n=n%100
    D=n//10
    n=n%10
    U=n
    if M!=0:
        print(M,'M','+',C,'C','+',D,'D','+',U,'U')
    elif M==0 and C!=0:
        print(C,'C','+',D,'D','+',U,'U')
    elif M==0 and C==0:
        print(D,'D','+',U,'U')
    elif M==0 and C==0 and D==0:
        print(U,'U')
    else:
        print("0")     