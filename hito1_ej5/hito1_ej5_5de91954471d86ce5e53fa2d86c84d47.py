#Cálculo del dígito verificador de un rut
rut = str(input("RUT "))
a = 3
sum = 0
suma = 0
resto = 0
dv = 0
contador = 0
for o in rut:
    contador = contador+1
if contador == 7:
      a = 2
      

for i in rut:
    
    sum = (int(a)*int(i))
    suma = suma+sum
    
    a=a-1
    
    if a == 1:
        a = 7
    
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'k'
print("dv ="+str(dv))

