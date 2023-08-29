# Entrada
A = int(input("Ingrese su primer dígito: "))
B = int(input("Ingrese su segundo dígito: "))
C = int(input("Ingrese su tercer dígito: "))
N = ","

# Procesamiento
X = min(A , B , C)
Y = max(A , B , C)
Z = (A + B + C) - X - Y
 
# Salida
print("El orden es", X, N, Z, N, Y)