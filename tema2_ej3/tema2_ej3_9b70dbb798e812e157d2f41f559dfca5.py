def numero_perfecto(a):
  global s
  s=0
  for n in range(1,a):
    x=a%n
    float(x)
    if x==0:
      s=n+s
  if a==s:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           