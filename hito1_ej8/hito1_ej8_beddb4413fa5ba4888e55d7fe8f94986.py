#Descomponer un número
UNITS = "UDCM"

num = input()[::-1]

output = []
for n, u in zip(num, UNITS):
  output.append(n+u)
  
print(" + ".join(output[::-1]))