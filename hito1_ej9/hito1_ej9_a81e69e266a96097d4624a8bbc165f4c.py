#Sistema de Ecuaciones
n1 = int(input("Coloque aquí el primer número: "))
n2 = int(input("Coloque aquí el segundo número: "))
n3 = int(input("Coloque aquí el tercero número: "))
n4 = int(input("Coloque aquí el cuarto número: "))
n5 = int(input("Coloque aquí el quinto número: "))
n6 = int(input("Coloque aquí el sexto número: "))

re = (n6*n1)-(n4*n3)
te = (n1*n5)-(n4*n2)

y = re/te

ni = n3-n2*y
do = n1

x = ni/do
y = round(y,1)
x = round(x,1)

print('x=',x)
print('y=',y)