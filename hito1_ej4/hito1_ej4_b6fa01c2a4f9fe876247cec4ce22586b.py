n = int(input())
binario = " "


while(n > 0):
  residuo = n%2
  binario += str(residuo)
  n = n // 2

binario2 = binario

binario = binario2[len(binario2):0:-1]

print("resultado =",binario)   