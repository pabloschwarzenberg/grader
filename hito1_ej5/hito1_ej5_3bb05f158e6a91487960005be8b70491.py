#Cálculo del dígito verificador de un rut
r= input("Ingrese su rut sin digito verificador ni puntos: ")

a= int(r[-1])
b= int(r[-2])
c= int(r[-3])
d= int(r[-4])
e= int(r[-5])
f= int(r[-6])
g= int(r[-7])



n1=a*2 
n2=b*3 
n3=c*4 
n4=d*5
n5=e*6 
n6=f*7 
n7=g*2 



x= n1+n2+n3+n4+n5+n6+n7
r= int(x/11)
q= x-(11*r) 

j= 11-q

if(j==11):
  print("dv= 0")
elif(j==10):
  print("dv= K")
else:
  print("dv= ",j)
 
x2= n1+n2+n3+n4+n5+n6+n7
z2= int(x2/11)
q2= x2-(11*z2) 
j2= 11-q2

if(len(r)==7):
  if(j2==11):
    print("dv= 0")
  elif(j2==10):
    print("dv= K")
  else:
    print("dv= ",j2)