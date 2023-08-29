#Cálculo del dígito verificador de un rut
rut=input("Ingrese RUT:")
rut=str(rut)
numero=2
suma=0
for i in rut[::-1]:
        x=int(i)*numero
        numero=numero+1
        suma=suma+x
        if numero==8:
            numero=2
z=suma%11
if z==0:
  print("dv=0")
else:
  digito=11-z
  if digito!=10:
    print("dv=",digito)
  elif digito==10:
    print("dv=k")
    