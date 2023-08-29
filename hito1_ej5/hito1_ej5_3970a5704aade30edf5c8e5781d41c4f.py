dg = str(input("ingrese rut sin digito verificador: "))
if len(dg) == 8:
    sub0 = int(dg[0:1])*3
    sub1 = int(dg[1:2])*2
    sub2 = int(dg[2:3])*7
    sub3 = int(dg[3:4])*6
    sub4 = int(dg[4:5])*5
    sub5 = int(dg[5:6])*4
    sub6 = int(dg[6:7])*3
    sub7 = int(dg[7:8])*2
    suma = sub0+sub1+sub2+sub3+sub4+sub5+sub6+sub7
elif len(dg) < 8:
    sub0 = int(dg[0:1])*2
    sub1 = int(dg[1:2])*7
    sub2 = int(dg[2:3])*6
    sub3 = int(dg[3:4])*5
    sub4 = int(dg[4:5])*4
    sub5 = int(dg[5:6])*3
    sub6 = int(dg[6:7])*2
    suma = sub0+sub1+sub2+sub3+sub4+sub5+sub6
mod = suma % 11
dv = 11-mod
if dv == 10:
  print("dv=K")
if dv == 11:
  print("dv=0")
else:
  print("dv=",dv)
