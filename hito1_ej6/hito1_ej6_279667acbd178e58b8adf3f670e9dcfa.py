#Ordenar tres números
x = int(input('Ingrese el primer número: '))
y = int(input('Ingrese el segundo número: '))
z = int(input('Ingrese el tercer número: '))
lista_numeros = [x,y,z]

a = min(lista_numeros)
b = max(lista_numeros)
c = (x + y + z) - (a + b)
print(a,c,b, sep=',')