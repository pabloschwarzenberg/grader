#Cálculo del dígito verificador de un rut
rut=input("Ingrese su rut")
if len(rut)==8:
   a=int(rut[7])
   b=int(rut[6])
   c=int(rut[5])
   d=int(rut[4])
   e=int(rut[3])
   f=int(rut[2])
   g=int(rut[1])
   h=int(rut[0])
   sumaproducto=a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3
   parteentera=int(sumaproducto/11)
   modulo11=(parteentera*11)
   restodivision=(sumaproducto-modulo11)
   codigo=(11-restodivision)
   if codigo==11:
    print("dv=0")
   else:
    if codigo==10:
        print("dv=K")
    else:
        print("dv=",codigo)
else: 
   a=int(rut[6])
   b=int(rut[5])
   c=int(rut[4])
   d=int(rut[3])
   e=int(rut[2])
   f=int(rut[1])
   g=int(rut[0])
   sumaproducto=a*2+b*3+c*4+d*5+e*6+f*7+g*2
   parteentera=int(sumaproducto/11)
   modulo11=(parteentera*11)
   restodivision=(sumaproducto-modulo11)
   codigo=(11-restodivision)
   if codigo==11:
    print("dv=0")
   else:
    if codigo==10:
        print("dv=K")
    else:
        print("dv=",codigo)     