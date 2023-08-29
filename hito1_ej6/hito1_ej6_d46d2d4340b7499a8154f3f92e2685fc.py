#Ordenar tres números
x = int(input("Ingrese primer numero:"))
y = int(input("Ingrese segundo numero:"))
z = int(input("Ingrese tercer numero:"))

Pa = max(x,y,z)
pe = min(x,y,z)
h = (x + y + z) - Pa - pe

print(pe ," , ", h ,", ",Pa)
    