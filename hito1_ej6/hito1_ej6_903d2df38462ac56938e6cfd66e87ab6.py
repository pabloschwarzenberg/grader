x = eval(input("Ingrese el primer número: "))
y = eval(input("Ingrese el segundo número: "))
z = eval(input("Ingrese el tercer número: "))
Ma = max(x, y, z)
Mi = min(x, y, z)
Mid = (x + y + z) - Ma - Mi
print("Los números ordenados de menor a mayor son ", Mi,",", Mid, ",", Ma)