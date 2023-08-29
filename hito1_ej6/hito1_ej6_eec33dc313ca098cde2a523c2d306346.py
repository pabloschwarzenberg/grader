#Ordenar tres números
n1 = int(input("Numero1: "))
n2 = int(input("Numero2: "))
n3 = int(input("Numero3: "))

a = min(n1, n2, n3)
c = max(n1, n2, n3)
b = ( n1 + n2 + n3) - a - c

print (a, b, c)
      