def numeros_binarios(n,i=0):
    b = bin(i)
    if len(b)>n+2:
        return
    elif len(b)<n+2:
        print('0'*(5-len(b))+b[2:])
        i+=1
    elif len(b)==n+2:
        print(b[2:])
        i+=1
    numeros_binarios(n,i)

n = int(input('Ingresa un número natural: '))
numeros_binarios(n)
           