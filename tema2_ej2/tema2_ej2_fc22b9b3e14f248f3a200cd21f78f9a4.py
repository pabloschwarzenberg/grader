# completa el código de la función
def amigos(a,b):
  numero1=corroborar_num(a,b)
  numero2=corroborar_num(b,a)
  if numero1 and numero2:
    return(True)
  return(False)

def corroborar_num(num,num2):
  suma=0
  
  for i in range(1,num):
    if num%i==0:
      suma+=i
  if suma==num2:
    return(True)
  return(False)

