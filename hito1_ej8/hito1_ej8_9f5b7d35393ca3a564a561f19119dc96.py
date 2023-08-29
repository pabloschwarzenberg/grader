#Descomponer un número
n=eval(input('Ingresa un numero: '))

m=(n//1000)
c=(n//100%10)
d=(n//10%10)
u=(n%10)

if 999<n<=9999:
    print(str(m)+'M','+', str(c)+'C','+', str(d)+'D','+', str(u)+'U')

if 99<n<=999:
    print(str(c)+'C','+', str(d)+'D','+', str(u)+'U')   

if 9<n<=99:
    print(str(d)+'D','+', str(u)+'U')

elif 0<n<=9:
    print(str(u)+'U')
