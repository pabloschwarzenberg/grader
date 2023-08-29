def rot13(palabra):
   rot1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
   rot2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
   cifrado=[]
   lis=[]
   nueva=""
   for i in palabra:
      if i in rot1:
          
          for k in range(0,12):
           if rot1[k]==i:
               lis.append(rot2[k])
           
      elif i in rot2:
          for k in range(1,13):
           if rot2[k]==i:
               lis.append(rot1[k]) 
   for t in lis:
         print(t)
         nueva=nueva+str(t)

   return  nueva  
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           