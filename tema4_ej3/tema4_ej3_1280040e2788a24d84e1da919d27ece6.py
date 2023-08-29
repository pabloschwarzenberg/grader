def jerigonzo(string):
 L=list(string)
 contador=0
 for x in L:
  if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
   L[contador]=x+"p"+x
  contador+=1 
 string=''.join(L)
 return string         