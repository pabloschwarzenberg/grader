# completa el código de la función
def suma(a):
  x=0
  for i in range(1,a):
    if a%i==0:
      x=x+i
  return x
   
def suma_divisores(a):
  if suma(a)==1:
    return (suma(a),True)
  else:
    return (suma(a),False)
if __name__ == "__main__":
    pass