#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese rut: "))
# 12345678
# a=1 b=2 c=3 d=4 e=5 f=6 g=7 h=8
# Conversion de string a numero y multiplicación
h=0
if(rut>9999999):
   rut=str(rut)
   a=(int(rut[0]))*3
   b=(int(rut[1]))*2
   c=(int(rut[2]))*7
   d=(int(rut[3]))*6
   e=(int(rut[4]))*5
   f=(int(rut[5]))*4
   g=(int(rut[6]))*3
   h=(int(rut[7]))*2
   suma=a+b+c+d+e+f+g+h
elif(rut<=9999999):
   rut=str(rut)
   a=(int(rut[0]))*2
   b=(int(rut[1]))*7
   c=(int(rut[2]))*6
   d=(int(rut[3]))*5
   e=(int(rut[4]))*4
   f=(int(rut[5]))*3
   g=(int(rut[6]))*2
   suma=a+b+c+d+e+f+g
# Resto (Algoritmo 1)
resto=suma%11
# Digito verificador (Algoritmo 1)
digito=11-resto
# Condiciones
if(digito==10):
    print("dv=k")
elif(digito==11):
    print("dv=0")
else:
    print("dv=",digito)