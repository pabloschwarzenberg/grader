secuencia=input()
n=int(input())
largo=len(secuencia)
if largo%n==0:
  veces=largo//n
  secuencia1=secuencia[0:veces]
  print(secuencia)
else:
  print("ninguna")