#Descomponer un número
n=int(input('valor de hasta 4 digitos:'))
m=n-(n%1000)
c=n-m-(n%100)
d=(n%100)-(n%10)
u=n%10
if n > 999 and n <= 9999:
    print('{0}M+{1}C+{2}D+{3}U' .format(m//1000,c//100,d//10,u))
elif n > 99 and n <= 999:
    print('{1}C+{2}D+{3}U' .format(m//1000,c//100,d//10,u))
elif n > 10 and n <= 99:
    print('{2}D+{3}U' .format(m//1000,c//100,d//10,u))
elif n >= 0 and n <= 10:
    print('{3}U' .format(m//1000,c//100,d//10,u))
else:
    print('ERROR')    
