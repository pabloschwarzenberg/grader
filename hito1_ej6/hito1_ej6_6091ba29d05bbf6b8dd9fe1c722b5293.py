#Ordenar tres números
def ordenar_numeros(n1,n2,n3):
    a = [n1,n2,n3];
    b = sorted(a);
    return b
print("ingrese el primer número:")
n1=int(input());
print("ingrese el segundo número:")
n2=int(input());
print("ingrese el tercer número:")
n3=int(input());
print(ordenar_numeros(n1,n2,n3));