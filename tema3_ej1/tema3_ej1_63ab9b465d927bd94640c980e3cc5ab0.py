# completa el código de la función
#def suma_divisores(a):
#  return
# completa el código de la función
def suma_divisores(a):
   div=[i for i in range(1,a) if a%i==0]
   m= sum(div)
   if m==1:
      return m,True
   return m,False