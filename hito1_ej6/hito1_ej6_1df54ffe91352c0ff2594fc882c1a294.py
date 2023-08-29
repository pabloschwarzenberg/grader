#Ordenar tres números
#entrada
x = eval(input("Ingrese el primer número: "))
y = eval(input("Ingrese el segundo número: "))
z = eval(input("Ingrese el tercer número: "))

#procedimiento
Ma = max(x, y, z)
Mi = min(x, y, z)
Mid = (x + y + z) - Ma - Mi

#salida
print("Los números ordenados de menor a mayor son ", Mi,",", Mid, ",", Ma)  