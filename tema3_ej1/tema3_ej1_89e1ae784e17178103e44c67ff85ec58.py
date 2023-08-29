# completa el código de la función
def suma_divisores(numero):
  sum_numero=0
  for i in range(1,numero):
    if numero%i==0:
      sum_numero=sum_numero+i
  if sum_numero==1:
    primo=True
    return (sum_numero,primo)
    
  else:
    primo=False
    return (sum_numero,primo)
      

if __name__ == "__main__":
  numero=int(input("Ingrese un numero: "))
  print(sumadivisores(numero))
  