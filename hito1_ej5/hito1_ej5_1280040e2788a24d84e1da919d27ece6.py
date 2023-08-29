#Cálculo del dígito verificador de un rut
rut=str(input("ingrese rut sin digito verificador"))                    
largo=len(rut)
d=len(rut)
h=len(rut)-1
contador=0
movimiento=0
serie=[2,3,4,5,6,7]
longitudserie=len(serie)
suma=0
while contador<largo:
 if movimiento>=len(serie):
  movimiento=movimiento-movimiento
 digito=int(rut[h:d])
 producto=digito*serie[movimiento]
 suma= suma + producto
 d=d-1
 h=h-1
 contador=contador+1
 movimiento=movimiento+1
else:
 resto=suma%11
 dv=11-resto
 if dv==11:
  print("dv=",0)
 elif dv==10:
  print("dv=","K")
 else:  
  print("dv=",dv)
