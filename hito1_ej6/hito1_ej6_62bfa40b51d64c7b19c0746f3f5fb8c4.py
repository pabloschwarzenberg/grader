#Ordenar tres números
x = int(input("escriba el primer numeros:" ))
n = int(input("escriba el segundo numero:" ))
z = int(input("escriba el tercer numero:" ))
a = min(x, n, z)
c = max(x, n, z)
b = (x + n + z) - a - c
print("el orden de sus numeros son:", (a, b, c))