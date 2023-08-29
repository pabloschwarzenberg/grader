# completa el código de la función
def amigos(a,b):
  divisiones_a= []
  for i in range(1,a):
    if a%i==0:
      i=divisiones_a.append(i)
  divisiones_b= []
  for i in range(1,b):
    if b%i==0:
      i=divisiones_b.append(i)
    
  print("divisiones A = ",divisiones_a)
  print("divisiones B =",divisiones_b)