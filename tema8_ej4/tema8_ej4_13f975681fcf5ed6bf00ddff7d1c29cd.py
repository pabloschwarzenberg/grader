def rot13(palabra):
   letra1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
   letra2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
   palabra_nueva=""
   espacio=" "
   for letra in palabra:
       j=0
       if letra in letra1:
           while j<len(letra1):
               if letra==letra1[j]:
                 palabra_nueva=palabra_nueva+letra2[j]
               j=j+1
       elif letra in letra2:
           while j<len(letra2):
               if letra==letra2[j]:
                   palabra_nueva=palabra_nueva+letra1[j]
               j=j+1
       else:
           palabra_nueva=palabra_nueva+espacio
    
   return palabra_nueva



           