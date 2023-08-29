#Ordenar tres números

# Entrada
x = int(input("Ingrese su primer dígito: "))
y = int(input("Ingrese su segundo dígito: "))
z = int(input("Ingrese su tercer dígito: "))

# Procesamiento

q = min(x , y , z)
w = max(x , y , z)
e = (x + y + z) - q - w
 
# Salida

print('El orden es:  {}, {}, {}'.format(q, e, w))