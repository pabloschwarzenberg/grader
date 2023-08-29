#Descomponer un número
a=int(input('ingrese numero:'))
b=int(str(a)[0])
if(a>=0 and a<=9):
    print(a,'U')
elif(a>=10 and a<=99):
    c = int(str(a)[1])
    print(b,'D','+',c,'U')
elif (a >= 100 and a <= 999):
    c = int(str(a)[1])
    d = int(str(a)[2])
    print(b, 'C', '+',c, 'D', '+', d, 'U')
elif (a >= 1000 and a <= 9999):
    c = int(str(a)[1])
    d = int(str(a)[2])
    e = int(str(a)[3])
    print(b, 'M', '+',c, 'C', '+', d, 'D', '+', e, 'U')
         