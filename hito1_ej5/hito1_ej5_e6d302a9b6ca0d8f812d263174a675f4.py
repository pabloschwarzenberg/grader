#Cálculo del dígito verificador de un rut
n=int(input("rut:"))
n1= n%10
n=n//10
x1= n1*2
n2=  n%10
n=n//10
x2= n2*3 
n3=  n%10
n=n//10
x3= n3*4
n4=  n%10
n=n//10
x4= n4*5
n5=  n%10
n=n//10
x5= n5*6
n6=  n%10
n=n//10
x6= n6*7 
n7=  n%10
n=n//10
x7= n7*2   
n8=  n%10
n=n//10
x8= n8*3
n9=  n%10
n=n//10
x9= n9*4
cal1= x1+x2+x3+x4+x5+x6+x7+x8+x9   
cal2= cal1//11
cal3= (cal1-(11*cal2))
vd= 11-cal3
if (vd==10):
  print("dv=K")
elif (vd==11):
  print("dv=0")
else:
  print("dv=", vd)  