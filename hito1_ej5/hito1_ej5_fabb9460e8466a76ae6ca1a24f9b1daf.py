#Gustavo Altez irarrazabal #Digito verificador RUT
Numerosos=str(input("inserte los numeros: "))
ruru=list(Numerosos)
Aux=int(Numerosos)
if Aux>=10000000:
  x1=ruru[7]
  x2=ruru[6]
  x3=ruru[5]
  x4=ruru[4]
  x5=ruru[3]
  x6=ruru[2]
  x7=ruru[1]
  x8=ruru[0]
  x1=int(x1)
  x2=int(x2)
  x3=int(x3)
  x4=int(x4)
  x5=int(x5)
  x6=int(x6)
  x7=int(x7)
  x8=int(x8)
  y1=x1*2
  y2=x2*3
  y3=x3*4
  y4=x4*5
  y5=x5*6
  y6=x6*7
  y7=x7*2
  y8=x8*3
  Yall=y1+y2+y3+y4+y5+y6+y7+y8 
  Yall1=Yall//11
  Yall2=Yall-(11*Yall1)
  final=Yall1-Yall2
  if final==11:
    print("dv=0")
  if final==9:
    print("dv=9")
  if final==8:
    print("dv=8")
  if final==7:
    print("dv=7")
  if final==6:
    print("dv=k")
  if final==5:
    print("dv=5")
  if final==4:
    print("dv=4")
  if final==3:
    print("dv=3")
  if final==2:
    print("dv=2")
  if final==1:
    print("dv=1")
  if final==0:
    print("dv=0")
  if final==10:
    print("dv=k")
if Aux<=9999999:
  x1=ruru[6]
  x2=ruru[5]
  x3=ruru[4]
  x4=ruru[3]
  x5=ruru[2]
  x6=ruru[1]
  x7=ruru[0]
  x1=int(x1)
  x2=int(x2)
  x3=int(x3)
  x4=int(x4)
  x5=int(x5)
  x6=int(x6)
  x7=int(x7)
  y1=x1*2
  y2=x2*3
  y3=x3*4
  y4=x4*5
  y5=x5*6
  y6=x6*7
  y7=x7*2
  Yall=y1+y2+y3+y4+y5+y6+y7
  Yall1=Yall//11
  Yall2=Yall-(11*Yall1)
  final=Yall1-Yall2
  if final==11:
    print("dv=0")
  if final==9:
    print("dv=9")
  if final==8:
    print("dv=0")
  if final==7:
    print("dv=3")
  if final==6:
    print("dv=6")
  if final==5:
    print("dv=5")
  if final==4:
    print("dv=4")
  if final==3:
    print("dv=3")
  if final==2:
    print("dv=2")
  if final==1:
    print("dv=1")
  if final==0:
    print("dv=0")
  if final==10:
    print("dv=k")