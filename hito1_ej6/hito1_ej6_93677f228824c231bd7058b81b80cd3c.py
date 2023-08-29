#ordenar tres numeros
print("Ingrese el primer numero")
a = int(input())
print("Ingrese el segundo numero")
b = int(input())
print("Ingrese el tercer numero")
c = int(input())

lista = [a, b, c]

lista.sort(reverse = False)

print(lista)