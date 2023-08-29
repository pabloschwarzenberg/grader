# completa el código de la función
def amigos(a,b):
  divisor_a=1
  suma_a=0
  divisor_b=1
  suma_b=0
  while divisor_a<=a:
    if a%divisor_a==0:
        suma_a=suma_a+divisor_a
    divisor_a=divisor_a+1
  while divisor_b<=b:
    if b%divisor_b==0:
        suma_b=suma_b+divisor_b
    divisor_b=divisor_b+1
  if suma_a==suma_b and a!=b:
    return True 
  else: 
    return False
    
   

           