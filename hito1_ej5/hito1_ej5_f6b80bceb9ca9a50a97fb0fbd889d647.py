rut = int(input("Ingrese rut sin Digito Verificador: "))
while not(rut>= 1000000 and rut<=99999999):
  rut = int(input("error Ingrese rut SIN Digito Verificador de 7 u 8 digitos: "))

vuelta = str(rut)[::-1]
largo = len(vuelta)

m1 = int(vuelta[0])*2
m2 = int(vuelta[1])*3
m3 = int(vuelta[2])*4
m4 = int(vuelta[3])*5
m5 = int(vuelta[4])*6
m6 = int(vuelta[5])*7
m7 = int(vuelta[6])*2
if(largo==8):
  m8= int(vuelta[7])*3
else:
  m8 = 0
suma = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8
modulo = suma%11
dv = 11-modulo
if (dv==10):
  dv = 'k'
if (dv == 11):
  dv = 0

print("dv =",dv)
