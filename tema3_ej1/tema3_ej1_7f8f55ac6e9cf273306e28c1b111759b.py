# completa el código de la función
def suma(a):
    suma=0
    i=1
    while i<a:
        if a%i==0:
          suma=suma+i
        i=i+1
    return suma
def suma_divisores(a):
  if suma(a)==1:
    return (suma(a),True)
  else:
    return (suma(a),False)
if __name__ == "__main__":
    pass
           