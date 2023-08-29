# completa el código de la función
def amigos(a,b):
    cont_div_a=0
    numeros_a=a
    while numeros_a>=1:
      if a%numeros_a==0:
        cont_div_a+=numeros_a
    cont_div_b=0
    numeros_b=b
    while numeros_b>=1:
      if b&numeros_b==0:
        cont_div_b+=numeros_b
      if cont_div_a==b and cont_di_b==a:
        return True
      else:
        return False
 
   

           