#Cálculo del dígito verificador de un rut
a=input()
b=len(a)
if b==8:
  suma=(int(a[0])*3+int(a[1])*2+int(a[2])*7+int(a[3])*6+int(a[4])*5+int(a[5])*4+int(a[6])*3+int(a[7])*2)
  resto=int(suma%11)
  r=int(11-resto)
  if 0<r<10:
    print("dv=",r)
  elif r==11:
    print("dv=0")
  else:
    print("dv=K")
if b==7:
  suma=(int(a[0])*2+int(a[1])*7+int(a[2])*6+int(a[3])*5+int(a[4])*4+int(a[5])*3+int(a[6])*2)
  resto=int(suma%11)
  r=int(11-resto)
  if 0<r<10:
    print("dv=",r)
  elif r==11:
    print("dv=0")
  else:
    print("dv=K")
  
  
  
  
  
  
  