num = int(input("Número decimal: "))

bits = []

while (num > 0):
  bits.append(str(num % 2))
  num //= 2

# Se usa la lista en reversa
bits = bits[::-1]

print("resultado=" + "".join(bits))