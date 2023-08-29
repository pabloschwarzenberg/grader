#Cálculo del dígito verificador de un rut
numero = int(input("Ingrese el rut sin el DV: ")) 

while not(numero>= 1000000 and numero<=99999999):
  numero = int(input("Ingrese el rut sin el DV de 7 u ocho dígitos: "))


a = str(numero)[::-1]
print("El número dado vuelta es: ",a)

uno = int(a[0])*2
dos = int(a[1])*3
tres = int(a[2])*4
cuatro = int(a[3])*5
cinco = int(a[4])*6
seis = int(a[5])*7
siete = int(a[6])*2
if(len(a)==8):
  ocho= int(a[7])*3
else:
  ocho = 0


sumatoria = uno + dos + tres + cuatro + cinco + seis + siete + ocho


resto = sumatoria%11


dv= 11 - resto
print(dv)

if (dv==10):
  dv = 'k'
if (dv == 11):
  dv = 0

print("dv =",dv)