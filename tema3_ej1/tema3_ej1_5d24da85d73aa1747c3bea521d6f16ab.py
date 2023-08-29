# completa el código de la función
def suma_divisores(a):
  d=1
  suma=0
  if a==1:
    return suma,False 
  while d<a:
    if a%d==0:
      suma+=d
      d+=1
    else:
       d+=1
  if suma>1:
    return suma, False
  elif suma == 1:
    return  suma,True
if __name__ == "__main__":
  a=3
  print(suma_divisores(a))
      
      
  
    
           