#Cálculo del dígito verificador de un ru
 assert type(numero) and type(digitos) == int
   if numero == 0:
      return 0
   elif numero//10 == 0:
      return digitos+1
   else: