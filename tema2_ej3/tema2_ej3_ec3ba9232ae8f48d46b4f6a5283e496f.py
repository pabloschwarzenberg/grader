def numero_perfecto(x):
    sumax=0
    for i in range(1,x):
        if x%i==0:
            sumax+=i

    return sumax==x 
if __name__ == "__main__":         
  n1=int(input('Introduzca el numero 1: '))
  z=0
  while z<=n1:
    z=z+1
    if numero_perfecto(z):
      print (z)
    else:
      continue

