#Ordenar tres números
 at = 3
numer = [0.] * at
for i in range(at):
  numer[i] = int(input("Ingrese su número: "))

for i in range(at-1):
  for j in range(i+1,at):
    if(numer[i] > numer[j]):
      cambio = numer[i]
      numer[i] = numer[j]
      numer[j] = cambio
for i in range(at):
  print(numer[i])