d = int(input("ingrese primer numero:"))
e = int(input("ingrese segundo numero:"))
f = int(input("ingrese tercer numero:"))

ME = min(d , e , f)
MA = max(d , e , f)

resultado = (d+ e + f) - MA - ME

print("De menor a mayor el orden es: ", ME, " , " , resultado, ", " , MA)