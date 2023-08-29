numero = int(input())
bin = []

loop = numero

while numero != 0:
  for x in range(numero):
    dif = numero - 2**x
    if dif == 1 or dif == 0:
      bin.append(dif)
      numero = dif
      break
      
print("".join(bin))