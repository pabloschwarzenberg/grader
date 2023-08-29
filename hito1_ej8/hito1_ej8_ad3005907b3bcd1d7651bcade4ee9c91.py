#Descomponer un número
      num = int(input("Please give me a number: "))
thou = int((num // 1000))
print("M",thou)

hun = int((num // 100))
print("C",hun)
ten =int((num // 10))
print("D",ten)
one = int((num // 1))
print("U",one)