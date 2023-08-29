#Nota final
PT=float(input("Ingrese nota 1: "))
PI=float(input("Ingrese nota 2: "))
NE=float(input("Ingrese nota 3: "))
PP=float(input("Ingrese nota 4: "))
formula=(0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
promedio=round(formula,1)
print(promedio)     