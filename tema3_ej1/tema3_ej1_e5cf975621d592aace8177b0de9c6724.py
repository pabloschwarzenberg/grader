# completa el código de la función
def suma_divisores(a):
  lstdiva=[i for i in range(1,a) if a %i==0]
  sd=0
  for _ in lstdiva:
    sd= sd + _

  if sd==1:
    return (sd,True)
  else:
    return (sd,False)

if __name__ == "__main__":
  a=int(input("numero: "))
  print (suma_divisores(a))
           