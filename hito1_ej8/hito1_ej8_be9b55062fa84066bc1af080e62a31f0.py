#Descomponer un número
#facil ya que volvemos al mismo recurso del problema dvrut
R=str(input()) #1234
if(int(R)>999):
  i=int(R[0:1]) 
  b=int(R[0:2])
  j=b-10*i
  c=int(R[0:3])
  k=c-10*b
  d=int(R[0:4])
  l=d-10*c
  a=str(i)
  b=str(j)
  c=str(k)
  d=str(l)
  print(a+"M","+",b+"C","+",c+"D","+",d+"U")

if(99<int(R)<1000):
  i=int(R[0:1]) 
  b=int(R[0:2])
  j=b-10*i
  c=int(R[0:3])
  k=c-10*b
  a=str(i)
  b=str(j)
  c=str(k)
  print(a+"C","+",b+"D","+",c+"U") 

if(9<int(R)<100):
  i=int(R[0:1]) 
  b=int(R[0:2])
  j=b-10*i
  a=str(i)
  b=str(j)
  print(a+"D","+",b+"U")
    
if(0<=int(R)<10):
  i=int(R[0:1]) 
  a=str(i)
  print(a+"U")
    

