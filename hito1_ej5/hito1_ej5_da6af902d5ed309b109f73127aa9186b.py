rut=input("Ingrese su rut:")
if int(rut)<999999:
  suma=int(rut[-1])*(2)+int(rut[-2])*(3)+int(rut[-3])*(4)+int(rut[-4])*(5)+int(rut[-5])*(6)+int(rut[-6])*(7)
elif int(rut)<9999999:
  suma=int(rut[-1])*(2)+int(rut[-2])*(3)+int(rut[-3])*(4)+int(rut[-4])*(5)+int(rut[-5])*(6)+int(rut[-6])*(7)+int(rut[-7])*(2)
elif int(rut)<99999999:
  suma=int(rut[-1])*(2)+int(rut[-2])*(3)+int(rut[-4])*(5)+int(rut[-5])*(6)+int(rut[-6])*(7)+int(rut[-7])*(2)+int(rut[-8])*(3)+int(rut[-3])*(4)

dv= 11 - suma%11
if dv==11:
  print("dv=",0)
elif dv==10:
  print("dv=","K")
else:
  print("dv=",dv)