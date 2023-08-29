#Cálculo del dígito verificador de un rut
rut=str(input("ingrese rut: "))

if len(rut) == 7:
 b = rut[0:1:1]
 c = rut[1:2:1]
 d = rut[2:3:1]
 e = rut[3:4:1]
 f = rut[4:5:1]
 g = rut[5:6:1]
 h = rut[6:7:1]

 j = int(b) * 2
 k = int(c) * 7
 l = int(d) * 6
 m = int(e) * 5
 n = int(f) * 4
 o = int(g) * 3
 p = int(h) * 2

 r = j + k + l + m + n + o + p
 s = r % 11
 dv = 11 - s

 if (dv == 10):
  print("dv=k")
 elif (dv==11):
  print("dv=0")
 else:
  print("dv= "+str(dv)+"")

elif len(rut)==8:
 b=rut[0:1:1]
 c=rut[1:2:1]
 d=rut[2:3:1]
 e=rut[3:4:1]
 f=rut[4:5:1]
 g=rut[5:6:1]
 h=rut[6:7:1]
 i=rut[7:8:1]

 j=int(b)*3
 k=int(c)*2
 l=int(d)*7
 m=int(e)*6
 n=int(f)*5
 o=int(g)*4
 p=int(h)*3
 q=int(i)*2

 r=j+k+l+m+n+o+p+q
 s=r%11
 dv=11-s

 if(dv==10):
  print("dv=k")
 elif (dv==11):
  print("dv=0")
 else:
  print("dv= "+str(dv)+"")