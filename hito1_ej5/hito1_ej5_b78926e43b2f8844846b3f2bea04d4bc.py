
a=input("¿cuál es tu rut sin guión? ")
if len(a)==8:
      b=11-(((int(a[7])*2+int(a[6])*3+int(a[5])*4+int(a[4])*5+int(a[3])*6+int(a[2])*7+int(a[1])*2+int(a[0])*3))%11)
      if b==10:
          print("dv=k")
      elif b==11:
          print("dv= 0")
      else:
          print ("dv= ",b)
elif len(a)==7:
      b=11-(((int(a[6])*2+int(a[5])*3+int(a[4])*4+int(a[3])*5+int(a[2])*6+int(a[1])*7+int(a[0])*2))%11)
      if b==10:
          print("dv=k")
      elif b==11:
          print("dv= 0")
      else:
         print ("dv= ",b)
else:
    print("Por favor, ingrese un rut válido ")
    
    

      