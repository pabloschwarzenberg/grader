m=input("su rut sin digito verificador: ")
n=list(m)
if len(n)==8:
  numero1=int(n[0])*3
  numero2=int(n[1])*2
  numero3=int(n[2])*7
  numero4=int(n[3])*6
  numero5=int(n[4])*5
  numero6=int(n[5])*4
  numero7=int(n[6])*3
  numero8=int(n[7])*2
  numero=numero1+numero2+numero3+numero4+numero5+numero6+numero7+numero8
  resto=numero%11
  digito=11-resto
elif len(n)==7:
  numero1=int(n[0])*2
  numero2=int(n[1])*7
  numero3=int(n[2])*6
  numero4=int(n[3])*5
  numero5=int(n[4])*4
  numero6=int(n[5])*3
  numero7=int(n[6])*2
  numero=numero1+numero2+numero3+numero4+numero5+numero6+numero7
  resto=numero%11
  digito=11-resto
if digito==11:
  print("dv=0")
elif digito==10:
  print("dv=k")
else:
  print("dv=",digito)
 