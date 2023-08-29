#Cálculo del dígito verificador de un rut
RUT=int(input("Ingresar RUT para obtener codigo verificador: "))

if RUT/10000000 >= 1:
  Primero=int(RUT/10000000)
  Segundo=int(RUT/1000000)%10
  Tercero=int(RUT/100000)%10
  Cuarto=int(RUT/10000)%10
  Quinto=int(RUT/1000)%10
  Sexto=int(RUT/100)%10
  Septimo=int(RUT/10)%10
  Octavo=RUT%10

  Codigo=11-(((Octavo*2)+(Septimo*3)+(Sexto*4)+(Quinto*5)+(Cuarto*6)+(Tercero*7)+(Segundo*2)+(Primero*3))%11)
  
  if Codigo == 10:
    print("dv=k")
  else:
    print("dv=",Codigo)
  
if 0 < RUT/10000000 < 1:
   A=int(RUT/1000000)
   B=int(RUT/100000)%10
   C=int(RUT/10000)%10
   D=int(RUT/1000)%10
   E=int(RUT/100)%10
   F=int(RUT/10)%10
   G=RUT%10
   
   Verificador=11-(((G*2)+(F*3)+(E*4)+(D*5)+(C*6)+(B*7)+(A*2))%11)
   
   if Verificador == 11:
     print("dv=0")
    
   else:
     print("dv=",Verificador)
   
