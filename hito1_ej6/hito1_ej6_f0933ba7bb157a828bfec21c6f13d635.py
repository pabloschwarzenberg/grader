# Entrada

a = int(input("Ingrese valor de a: "))
b = int(input("Ingrese valor de b: "))
c = int(input("ingrese valor de c: "))

#Condiciones

if a <= b and a <= c and b <= c:
    Resultado = a, b, c
elif b <= a and b <= c and a <= c:
    Resultado = b, a, c
elif a <= c and a <= b and c <= b:
    Resultado = a, c, b
elif b <= c and b <= a and c <= a:
    Resultado = b, c, a
elif c <= a and c <= b and a <= b:
    Resultado = c, a, b
else:
    Resultado = c, b, a

#Final

print("El orden de los números de menor a mayor es:", Resultado)
    

      