#Cálculo del dígito verificador de un rut
rut = int(input("ingresa rut sin numero verificador: "))

strnum = str(rut)[::-1]

n1= int(strnum[0])*2
n2= int(strnum[1])*3
n3= int(strnum[2])*4
n4= int(strnum[3])*5
n5= int(strnum[4])*6
n6= int(strnum[5])*7
n7= int(strnum[6])*2
if (len (strnum)==8):
    n8=int(strnum[7])*3
else:
    n8=0

suma = n1+n2+n3+n4+n5+n6+n7+n8

resto = suma%11

dv = 11- resto

if (dv==10):
    dv = "k"
if (dv == 11 ):
    dv = 0
print ("dv =",dv)
      