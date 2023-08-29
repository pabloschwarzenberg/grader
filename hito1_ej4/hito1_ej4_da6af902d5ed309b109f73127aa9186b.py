numera=int(input("Ingrese un número:"))
repeticion = 0
resultado = 0

while numera != 0:
  if numera%2 == 1:
    binario = 1
  else:
    binario=0
  numera=numera//2
  final=binario*10**(repeticion)
  resultado += final
  repeticion += 1
print("resultado=",resultado)
