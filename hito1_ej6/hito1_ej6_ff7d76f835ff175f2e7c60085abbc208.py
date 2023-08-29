#Orden de tres números

a = int(input("Inserte un número a >>> "))
b = int(input("Inserte un n´mero b >>> "))
c = int(input("Inserte un número c >>> "))

x = min(a, b, c)
y = max(a, b, c)
z = (a + b + c) - x - y

print("Ordenados de menor a mayor: {}, {}, {}".format(x, z, y))