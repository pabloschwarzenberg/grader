def amigos(uno,dos):
 contador1=0
 contador2=0
 i=1

 while i<uno:
    if uno%i==0:
        
        contador1 = contador1 + i
    i=i+1  
 
    
 i=1
 while i<dos:
    if dos%i==0:
       
        contador2 = contador2 + i
    
    i=i+1
 

 if contador1==dos and contador2==uno:
     return True
 else: return False
if __name__ == "__main__":
  uno=int(input('Ingrese el primer número: '))
  dos=int(input('Ingrese el segundo número: '))
  f=amigos(uno,dos)
  print(f)