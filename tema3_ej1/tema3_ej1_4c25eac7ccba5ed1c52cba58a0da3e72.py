# completa el código de la función
def suma_divisores(a):
  numero=a-1
  val=0
  while (numero>0):
    if a%numero==0:
      val+=numero
    numero=numero-1
  if val!=1:
    return(val, False)
  else:
    return(val, True)
    
if __name__ == "__main__":
  print(suma_divisores(17))