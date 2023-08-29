# completa el código de la función
def amigos(a,b):
     div_de_numero1 = 1
   div_de_numero2 = 1
   sum_div_numero1 = 0
   sum_div_numero2 = 0
   while div_de_numero1 < a:
      if a%div_de_numero1 == 0:
         suma_div_numero1 += div_de_numero1
      div_de_numero1 += 1
   while div_de_numero2 < b:
      if b%div_de_numero2 == 0
         suma_div_numero2 += div_de_numero2
      div_de_numero2 += 1
   if sum_div_numero1 == b and sum_div_numero2 == a:
      return True
   else:
      return False
try:
   numero1 = int(input("Numero 1:"))
   numero2 = int(input("Numero 2:"))
   print(amigo(numero1,numero2))
except:
   print("Por favor Ingrese un numero")
           