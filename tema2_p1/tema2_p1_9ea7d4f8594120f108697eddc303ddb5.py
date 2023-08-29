# por favor escribe aquí tu función
def es_primo(num):
 for i in range(num):
   modulo = num%(i+1)
   if i+1 != 1 and i+1 != num and modulo == 0 or num == 1 or num == 0:
     primo = False
     break
   primo = True
 if num == 0:
   primo = False
 return primo
           