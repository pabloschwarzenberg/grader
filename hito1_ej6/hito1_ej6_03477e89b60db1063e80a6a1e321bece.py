#Ordenar tres números
a = int(input("ingresa numero: "))
b = int(input("ingresa numero: "))
c = int(input("ingresa numero: "))
if a <= b and a <= c:
    numero_menor = a
    if b <= c:
        numero_del_medio = b
        numero_mayor = c
    else:
        numero_del_medio = c
        numero_mayor = b
elif b <= a and b < c:
    numero_menor = b;
    if a <= c:
        numero_del_medio = a;
        numero_mayor = c;
    else:
        numero_del_medio = c;
        numero_mayor = a
else:
    numero_menor = c;
if a <= b:
        numero_del_medio = a;
        numero_mayor = b;
else:
        numero_del_medio = b
print(numero_menor, numero_del_medio, numero_mayor)