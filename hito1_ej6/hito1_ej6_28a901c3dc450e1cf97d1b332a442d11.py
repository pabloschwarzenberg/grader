#Ordenar tres números

x =int(input('Ingrese un primer número: '))
y =int(input('Ingrese un segundo número: '))
z =int(input('Ingrese un tercer numero: '))

if x>=y>=z:
    print(z, ' ,', y, ' ,', x )

if x>=z>=y:
    print(y, ' , ', z,' , ', x)
    
if y>=z>=x:
    print(x, ' , ', z, ' , ', y)
  
if y>=x>=z:
    print(z, ' , ', x, ' , ', y)

if z>=y>=x:
    print(x, ' , ', y, ' , ', z)
  
if z>=x>=y:
    print(y, ' , ', x,' , ',z)