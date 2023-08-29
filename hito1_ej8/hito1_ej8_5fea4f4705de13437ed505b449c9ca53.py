#Descomponer un número
numero= int(input('Ingrese un número entero de hasta 4 digitos: '))
s_numero= str(numero)
s1 = 'U'
s2 = 'DU'
s3 = 'CDU'
s4 = 'MCDU'
n = len(s_numero)
i=0
if n == 4:
    while i < n:
        print(s_numero[i] + s4[i], end=' ')
        if i!=n-1:
            print('+ ', end='')
        i+=1
elif n == 3:
    while i < n:
        print(s_numero[i] + s3[i], end=' ')
        if i!=n-1:
            print('+ ', end='')
        i+=1
elif n == 2:
    while i < n:
        print(s_numero[i] + s2[i], end=' ')
        if i!=n-1:
            print('+ ', end='')
        i+=1
elif n == 1:
    while i < n:
        print(s_numero[i] + s1[i], end=' ')
        if i !=n-1:
            print('+ ', end='')
        i+=1      