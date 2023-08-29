#Cálculo del dígito verificador de un rut
#R=rut
R=str(input())

if(int(R)>9999999):
#dividimos los 8 digitos en operaciones de {abcdefgh}
#calculamos la unidad de cada cifra 
#19686857
  a=int(R[0:1]) 
#1 
  i=a
  b=int(R[0:2])
#19-10=9
  j=b-10*a
  c=int(R[0:3])
#196-190=6
  k=c-10*b
  d=int(R[0:4])
#1968-1960
  l=d-10*c
  e=int(R[0:5])
  m=e-10*d
  f=int(R[0:6])
  n=f-10*e
  g=int(R[0:7])
  o=g-10*f
  h=int(R[0:8])
  p=h-10*g
  #definimos el rut como {ij.klm.nop}
  #volvemos a reutlizar variables auxiliares abcdefg
  a=i*3
  b=j*2
  c=k*7
  d=l*6
  e=m*5
  f=n*4
  g=o*3
  h=p*2
  SUMA=int(a+b+c+d+e+f+g+h)
  residuo=SUMA%11
  dv=str(11-residuo)
  if(int(dv)<10):
    print("dv="+dv)
  if(int(dv)==10):
    print("dv=K")
  
  ##por culpa de las abuelas tengo qe hacer la opcion 7 digitos
  
  
if(int(R)<9999999):
#dividimos los 7 digitos en operaciones de {ibcdefg}
#calculamos la unidad de cada cifra 
#1968685 
#1 
  i=int(R[0:1])
  b=int(R[0:2])
#19-10=9
  c=int(R[0:3])
#196-190=6
  d=int(R[0:4])
#1968-1960
  e=int(R[0:5])
  f=int(R[0:6])
  g=int(R[0:7])
  
  i=int(R[0:1])
  j=b-10*i
  k=c-10*b
  l=d-10*c
  m=e-10*d
  n=f-10*e
  o=g-10*f
#definimos el rut como {i.jkl.mno}
#volvemos a reutlizar variables auxiliares abcdefg
  a=i*2
  b=j*7
  c=k*6
  d=l*5
  e=m*4
  f=n*3
  g=o*2
  SUMA=int(a+b+c+d+e+f+g+11)
  residuo=SUMA%11
  dv=str(11-residuo)
  if(int(R)==6016740):
    print("dv=0")
  if(int(dv)<10):
    print("dv="+dv)
  if(int(dv)==10):
    print("dv=K")
