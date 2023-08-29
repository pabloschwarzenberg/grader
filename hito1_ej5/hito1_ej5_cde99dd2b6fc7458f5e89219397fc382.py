rut = input("ingrese rut sin verificador:  ")
rut2 = len(rut)
if rut2 == 7:
 rut3 = "0"+rut
elif rut2 == 8:
  rut3 = rut
r1 = int(rut3[:1])
r2 = int(rut3[1:2])
r3 = int(rut3[2:3])
r4 = int(rut3[3:4])
r5 = int(rut3[4:5])
r6 = int(rut3[5:6])
r7 = int(rut3[6:7])
r8 = int(rut3[7:8])
multi_suma = (r8*2)+(r7*3)+(r6*4)+(r5*5)+(r4*6)+(r3*7)+(r2*2)+(r1*3)
division = multi_suma/11
truncado = int(division)
multi_trunc = truncado*11
resta_trunc = multi_suma-multi_trunc
numero_verificador = 11-resta_trunc
if(numero_verificador == 11):
 print("dv = 0")
elif(numero_verificador == 10):
   print("dv = k")
else :
 print("dv = ", numero_verificador)
truncado = int(division)
multi_trunc = truncado*11
resta_trunc = multi_suma-multi_trunc
numero_verificador = 11-resta_trunc
if(numero_verificador == 11):
 print("dv = 0")
elif(numero_verificador == 10):
   print("dv = k")
else :
 print("dv = ", numero_verificador)