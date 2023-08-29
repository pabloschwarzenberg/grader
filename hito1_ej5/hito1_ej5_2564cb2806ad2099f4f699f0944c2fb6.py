#Cálculo del dígito verificador de un rut
a=str(input("Ingrese rut, sin dígito verificador:"))
if(len(a)==8):
   p=int(a[7])*2
   q=int(a[6])*3
   r=int(a[5])*4
   s=int(a[4])*5
   t=int(a[3])*6
   u=int(a[2])*7
   v=int(a[1])*2
   w=int(a[0])*3
   x=p+q+r+s+t+u+v+w
   z=(x%11)
   if(z==0):print("dv=0")
   else:
    y=11-(x%11)
    if(y==10):print("dv=k")
    else:
       if(y!=10):print("dv="+str(y))
       else:print("Rut no válido")
else:
    if (len(a)==7):
     q=int(a[6])*2
     r=int(a[5])*3
     s=int(a[4])*4
     t=int(a[3])*5
     u=int(a[2])*6
     v=int(a[1])*7
     w=int(a[0])*2
     x=q+r+s+t+u+v+w
     z=(x%11)
     if(z==0):print("dv=0")
     else:
      y=11-(x%11)
      if(y==10):print("dv=k")
      else:
         if(y!=10):print("dv="+str(y))
         else:print("Rut no válido")
