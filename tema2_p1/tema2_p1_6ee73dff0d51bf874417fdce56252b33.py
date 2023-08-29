# por favor escribe aquí tu función
def numero(a):
  numero=int(input("numero: "))
  divisor=1
  suma=0
  while divisor<=numero: 
   if numero%divisor==0:
      suma=suma+divisor
   divisor=divisor+1
  
  if(suma==numero+1):
    return
  