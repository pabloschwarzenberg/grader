#Descomponer un número
numero = input()
lista = ['M','C','D','U']
nueva_lista = []
suma = ''
for i in range(len(numero)):
    n = numero[-i-1]+lista[-i-1]
    nueva_lista.append(n)

for i in range(len(nueva_lista)):
    suma += nueva_lista[-i-1]+'+'
               
suma = suma.strip('+')    
print(suma)