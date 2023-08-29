secuencia=input()
n=int(input())
if len(secuencia) % 3 != 0:
  print("ninguna")
if len(secuencia) % 3 == 0:
  for i in range(0,len(secuencia)-3):
    print(secuencia[i:i+3])
