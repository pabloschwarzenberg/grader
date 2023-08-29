def rot13(palabra):
 L=list(palabra)
 x=0
 R1=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
 R11=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
 R2=["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
 R22=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
 for letra in L: 
  for contador in range(0,13):
   if(letra==R1[contador]):
    L[x]=R2[contador]
   elif(letra==R11[contador]):
    L[x]=R22[contador]
   elif(letra==R2[contador]):
    L[x]=R1[contador]
   elif(letra==R22[contador]):
    L[x]=R11[contador]
  x+=1    
 palabra=''.join(L)
 return palabra