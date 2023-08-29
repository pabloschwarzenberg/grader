#Ordenar tres numeros
x1=int(input('Ingrese un numero: '))
x2=int(input('Ingrese otro numero: '))
x3=int(input('Ingrese un ultimo numero: '))
#primer valor
if x1>x2 and x1>x3:
  mayor=x1
if x2>x1 and x2>x3:
  mayor=x2
if x3>x2 and x3>x1:
  mayor=x3
#segundo valor
if x2>x1>x3 or x3>x1>x2:
  medio=x1
if x1>x2>x3 or x3>x2>x1:
  medio=x2
if x2>x3>x1 or x1>x3>x2:
  medio=x3
#tercer
if x3>x1 and x2>x1:
  menor=x1
if x1>x2 and x3>x2:
  menor=x2
if x2>x3 and x1>x3:
  menor=x3
print(str(menor)+','+str(medio)+','+str(mayor))