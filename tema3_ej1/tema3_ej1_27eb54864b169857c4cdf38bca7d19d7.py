# completa el código de la función
def suma_divisores(numero):
  i = 1
  s=0
  while i<numero:
    if numero%i==0:
      s=s+i
      i +=1
    else:
      i +=1
  if s==1:
    return s,True
  else:
    return s,False  
if __name__ == "__main__":  
  numero = int(input("Ingrese su numero:")) 
  print(suma_divisores(numero))
  