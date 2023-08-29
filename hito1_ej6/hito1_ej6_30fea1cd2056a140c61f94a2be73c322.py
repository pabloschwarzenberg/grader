
      Ordenar tres números

# Ordenar números de menor a mayor

x = int(input('Ingrese el primer número: 5'))
y = int(input('Ingrese el segundo número: 7'))
z = int(input('Ingrese el primer número: '1))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

print('{}, {}, {}'. format(a,b,c))    
