#Ordenar 3 números de menor a mayor 
n1 = int(input("Primer número:"))
n2 = int(input("Segundo número:"))
n3 = int(input("Tercer número:"))

mayor = max(n1 , n2 , n3)
menor = min(n1 , n2 , n3)
medio = n1 + n2 + n3 - menor - mayor

print(f"El orden seria {menor},{medio},{mayor}")