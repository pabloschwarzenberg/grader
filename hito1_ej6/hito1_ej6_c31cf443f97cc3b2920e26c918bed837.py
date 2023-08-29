A = int(input("Ingrese primer número:"))
B = int(input("Ingrese segundo número:"))
C = int(input("Ingrese tercer número:"))

x = min(A,B,C)
y = max(A,B,C)
z = (A+B+C) - x - y

print("Los números ingresados tienen el siguiente orden: {}, {}, {}".format(x,z,y)) 