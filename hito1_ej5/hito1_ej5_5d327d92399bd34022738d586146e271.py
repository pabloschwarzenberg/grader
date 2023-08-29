#Cálculo del dígito verificador de un rut
print("rut")
r=("20334364")
str=(r)
m=((int(r[7])*2)+(int(r[6])*3)+(int(r[5])*4))
y=((int(r[4])*5)+(int(r[3])*6)+(int(r[2])*7))
z=((int(r[1])*2)+(int(r[0])*3))
h=(y)+(z)+(m)
w=(h)//11
x=(11-((h)-(11*(w))))
if int(x)== 11 :
  print("dv=0")
elif int(x) == 10: 
  print("dv=K")
else:
  print("dv=",(x))  
