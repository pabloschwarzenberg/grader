# completa el código de la función
def amigos(a,b):
     da=0
     db=0
     if a!=b:
         for divisor in range(1,a+1):
             if a%divisor==0:
                 da=da+divisor
         for divisor in range(1,b+1):
             if b%divisor==0:
                db=db+divisor
         if da==db:
             return True
         elif da!=db:
             return False
     else:
         return False
           