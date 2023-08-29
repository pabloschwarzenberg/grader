#Cálculo del dígito verificador de un rut
rut=int(input("ingrese numero de rut:"))

if(1000000<=rut<=9999999):
    rut = str(rut)
    n1=int(rut[0])*9
    n2=int(rut[1])*4
    n3=int(rut[2])*5
    n4=int(rut[3])*6
    n5=int(rut[4])*7
    n6=int(rut[5])*8
    n7=int(rut[6])*9
    N=(n1+n2+n3+n4+n5+n6+n7)
    N1=(N%11)
    if(0<=N1<=9):
      print("dv="+str(N1))
    if(N1==10):        
      print("dv=K")
elif(10000000<=rut<=99999999):
    rut = str(rut)
    n1=int(rut[0])*8
    n2=int(rut[1])*9
    n3=int(rut[2])*4
    n4=int(rut[3])*5
    n5=int(rut[4])*6
    n6=int(rut[5])*7
    n7=int(rut[6])*8
    n8=int(rut[7])*9
    N=(n1+n2+n3+n4+n5+n6+n7+n8)
    N1=(N%11)
    if(0<=N1<=9):
      print("dv="+str(N1))
    if(N1==10):        
      print("dv=K")
else:
  print("rut invalido")
