# completa el código de la función
def amigos(a,b):
    div=1
    cdiv=0
    while a<= div or b<= div:
         if a%div==0 or b%div==0:
             div=div+1
             cdiv=cdiv+1
             return cdiv
   if (div*cdiv)==a or (div*cdiv)==b:
       return True
   else:
       return False
           