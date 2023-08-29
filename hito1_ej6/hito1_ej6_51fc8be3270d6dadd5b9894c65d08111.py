n1 =int(input("mencione un numero"))
n2 =int(input("mencione un numero"))
n3 =int(input("mencione un numero"))
a = min(n1, n2 , n3)
c = max(n1, n2 , n3)
b = (n1 + n2 + n3 ) - a - c
print("los numeros ordenados en {},{},{}".format(a , b , c))
  