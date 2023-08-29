#Descomponer un número
numero= int(input('ingrese numero de 4 cifras hacia abajo:'))

n1= numero%10
n2= (numero%100)//10
n3= (numero%1000)//100
n4= (numero%10000)//1000

a1= str(n1)
a2= str(n2)
a3= str(n3)
a4= str(n4)

if 1000 <= numero <= 9999:
    print(a4+'M','+', a3+'C','+', a2+'D','+', a1+'U')
elif 100 <= numero <= 999:
    print(a3+'C', '+', a2+'D', '+', a1+'U')
elif 10 <= numero <= 99:
    print(a2 + 'D', '+', a1 + 'U')
