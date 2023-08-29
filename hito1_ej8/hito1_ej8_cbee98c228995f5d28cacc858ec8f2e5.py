#Descomponer un número
x=int(input('ingrese un número entero de 4 cifras'))
a=x%10
b=(x//10)%10
c=(x//100)%10
d=(x//1000)
if 1000<=x<=9999:
        print(str(d)+'M','+',str(c)+'C','+',str(b)+'D','+',str(a)+'U')
if 100<=x<=999:
        print(str(c)+'C','+',str(b)+'D','+',str(a)+'U')
if 10<=x<=99:
        print(str(b)+'D','+',str(a)+'U')
if 0<=x<=9:
        print(str(a)+'U')
