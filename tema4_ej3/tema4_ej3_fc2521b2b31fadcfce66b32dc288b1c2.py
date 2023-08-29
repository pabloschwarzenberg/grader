def jerigonzo(string):
   palabra=list(string)
   vocales=["a","e","i","o","u"]
   for i in palabra:
     for j in vocales:
       if j==i:
         palabra[palabra.index(i)]=i+"p"+j
   palabra="".join(palabra)
   
   return palabra