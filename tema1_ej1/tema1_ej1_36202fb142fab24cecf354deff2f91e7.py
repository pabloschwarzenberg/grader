
#usando la formula: n * (n+1) / 2
print("ingresa un numero")     
n = int(input())

suma = n* (n + 1)/2

print(suma)
print()

#usando un ciclo
suma = 0
for i in range(1, n + 1):
    suma += i
    
print(suma)

print()

#usar funcion sum:

suma= sum(range(1, n + 1))

print(suma)

      