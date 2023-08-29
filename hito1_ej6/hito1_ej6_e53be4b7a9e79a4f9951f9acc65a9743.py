#Ordenar tres números
x = int(input('Ingrese el primer digito entero: '))
y = int(input('Ingrese el segundo digito entero: '))
z = int(input('Ingrese el tercer digito entero: '))    

menor = min(x, y, z)
maximo = max(x, y, z)
intermedio = (x + y + z) - menor - maximo

print(menor,intermedio,maximo,sep=',')