#Cálculo del dígito verificador de un rut
num = int(input("Ingrese rut SIN DV: ")) #20023066
#Validar que el número sea de 7 o de 8 caracteres
while not(num>= 1000000 and num<=99999999):
  num = int(input("Ingrese rut SIN DV de 7 u ocho digitos: "))

#1) Dar vuelta el número  ==>     66023002
a = str(num)[::-1]
print("Numero dado vuelta: ",a)
#2) multiplicar cada digito por la serie 2, 3, 4, 5, 6, 7 , 2, 3, ....
uno = int(a[0])*2
dos = int(a[1])*3
tre = int(a[2])*4
cua = int(a[3])*5
cin = int(a[4])*6
sei = int(a[5])*7
sie = int(a[6])*2
if(len(a)==8):
  och= int(a[7])*3
else:
  och = 0
#3) Sumamos todos los resultados de las multiplicaciones anteriores:

suma = uno + dos + tre + cua + cin + sei + sie + och

#4) Obtener el resto de la división de suma anterior por 11: suma%11

resto = suma%11

#5) el dv es = 11 menos el resto (calculado en 4):

dv= 11 - resto
print(dv)

#6) preguntar si dv==10 entonces dv='k'.
if (dv==10):
  dv = 'k'

#7) preguntar si dv==11 entonces dv=0.
if (dv == 11):
  dv = 0

print("dv =",dv)