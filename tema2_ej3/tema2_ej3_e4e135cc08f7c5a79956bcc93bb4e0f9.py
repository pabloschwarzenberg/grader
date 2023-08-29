def numero_perfecto(a):
  x=1
  z=0
  while(x<a):
    j=a%x
    if(j==0):
      z=z+x      
      x=x+1
    else:
      x=x+1
  if(z==a):   
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           