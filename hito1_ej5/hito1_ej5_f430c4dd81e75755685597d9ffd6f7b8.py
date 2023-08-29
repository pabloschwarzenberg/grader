#Cálculo del dígito verificador de un rut
ingrese="SI"
while ingrese=="SI":
   rut=list(input("Ingrese los primeros 8 dígitos de su RUT:"))
   a=int(rut[0])*3
   b=int(rut[1])*2
   c=int(rut[2])*7
   d=int(rut[3])*6
   e=int(rut[4])*5
   f=int(rut[5])*4
   g=int(rut[6])*3
   h=int(rut[7])*2
   i=a+b+c+d+e+f+g+h
   j=i//11
   if i%11==1:
      print("El código verificador es: K")
   elif i%11!=1:
      print("El código verificador es: ", 11-(i%11))
   ingrese=input("Desea ingresar un nuevo rut?")
   ingrese=ingrese.upper()
