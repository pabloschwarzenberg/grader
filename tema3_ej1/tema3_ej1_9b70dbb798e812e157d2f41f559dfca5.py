# completa el código de la función
def suma_divisores(a):
  global s
  s=0
  for n in range(1,a):
    x=a%n
    float(x)
    if x==0:
      s=n+s
  if s==1:
    return (s,True)
  else:
    return (s, False)
if __name__ == "__main__":
  g=input("ingrese un numero: ")
  g=int(g)
  suma=suma_divisores(g)

  if s==1:
    print((s,True))
  else:
    print((s,False))
