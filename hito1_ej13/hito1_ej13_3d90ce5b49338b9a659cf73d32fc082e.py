nUsuario = int(input("Ingrese un numero: "))
count = 0
factores = []
for i in range (2, nUsuario+1):
    while nUsuario% i == 0:
        factores.append(i)
        nUsuario = nUsuario / i
for j in range(len(factores)):
  print(factores[j])