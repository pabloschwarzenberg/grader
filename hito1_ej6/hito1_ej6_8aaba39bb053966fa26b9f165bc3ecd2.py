x=int(input('ingresa el primer numero'))
y=int(input('ingresa el segundo numero'))
z=int(input('ingresa el tercer numero'))

menor=min(x,y,z)
mayor=max(x,y,z)
valor_medio=(x+y+z)- menor - mayor

print(menor,valor_medio,mayor)

print()

numeros= x,y,z
print(numeros)
numeros= sorted(numeros)
print(numeros)


