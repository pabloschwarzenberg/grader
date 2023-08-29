#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut sin digito verificador: "))
N1=((rut%10)*2)
N2=((rut//10%10)*3)
N3=((rut//100%10)*4)
N4=((rut//1000%10)*5)
N5=((rut//10000%10)*6)
N6=((rut//100000%10)*7)
N7=((rut//1000000%10)*2)
N8=((rut//10000000%10)*3)
suma=(N1+N2+N3+N4+N5+N6+N7+N8)
division=(suma//11)
resto=(suma-(division*11))
DV=(11-resto)
if(DV==11):
  print("dv=0")
elif(DV==10):
  print("dv=K")
else:
  print("dv=",DV)