#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese rut SIN DV: ")) 
while not(rut>= 1000000 and rut<=99999999):
  rut=int(input("Ingrese rut SIN DV de 7 u ocho digitos: "))
a=str(rut)[::-1]
print("Numero dado vuelta: ",a)
uno=int(a[0])*2
dos=int(a[1])*3
tre=int(a[2])*4
cua=int(a[3])*5
cin=int(a[4])*6
sei=int(a[5])*7
sie=int(a[6])*2
if(len(a)==8):
  och=int(a[7])*3
else:
  och=0
suma=uno+dos+tre+cua+cin+sei+sie+och
resto=suma%11
dv=11 - resto
print(dv)
if (dv==10):
  dv='k'
if (dv == 11):
  dv=0
print ("dv =",dv)