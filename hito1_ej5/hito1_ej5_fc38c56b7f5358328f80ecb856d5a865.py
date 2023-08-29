#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su numero de rut: "))

if(10000000<=rut<=99999999):
  rut=str(rut)
  x1=int(str(rut)[0])*8
  x2=int(str(rut)[1])*9
  x3=int(str(rut)[2])*4
  x4=int(str(rut)[3])*5
  x5=int(str(rut)[4])*6
  x6=int(str(rut)[5])*7
  x7=int(str(rut)[6])*8
  x8=int(str(rut)[7])*9
  X=(x1+x2+x3+x4+x5+x6+x7+x8)
  Y=(X%11)
  if(0<=Y<=9):
      print("dv="+str(Y))
  if(Y==10):
      print("dv=K")
   
elif(1000000<=rut<=9999999):
    rut=str(rut)
    x1=int(rut[0])*9
    x2=int(rut[1])*4
    x3=int(rut[2])*5
    x4=int(rut[3])*6
    x5=int(rut[4])*7
    x6=int(rut[5])*8
    x7=int(rut[6])*9
    X=(x1+x2+x3+x4+x5+x6+x7)
    Y=(X%11)
    if(0<=Y<=9):
       print("dv="+str(Y))
    if(Y==10):
       print("dv=K")
      
else:
    print("rut no valido")
   