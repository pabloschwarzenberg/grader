def amigos(a,b):
  l_a=0
  l_b=0
  for i in range(1,a):
    if a%i==0:
      l_a+=i
  for k in range(1,b):
    if b%k==0:
      l_b+=k
  if l_a==b and l_b==a:
    return True
  else:
    return False
    
def numero_perfecto(a):
  return amigos(a,a)
  


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           