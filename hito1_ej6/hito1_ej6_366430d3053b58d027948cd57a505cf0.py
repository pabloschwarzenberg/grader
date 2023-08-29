#Ordenar tres números
# Entrada
a = int(input("Ingrse numero: "))
b = int(input("Ingrse numero: "))
c = int(input("Ingrse numero: "))
# Proceso
if a >= c >= b:
    x = b, c, a
elif b >= a >= c:
    x = c, a, b
elif c >= b >= a:
    x = a, b, c
elif a >= b >= c:
    x = c, b, a
elif c >= a >= b:
    x = b, a, c
# Salida
print("Numero del menor al mayor:", x)