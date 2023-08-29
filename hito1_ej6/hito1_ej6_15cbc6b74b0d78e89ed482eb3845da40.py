print('ordenar tres numeros')
a = int(input('ingrese valor 1:'))
    
b = int(input('ingrese valor 2:'))

c = int(input('ingrese valor 3:'))
   
if((a <= b) and (a <= c)):
  menor = a;
  if (b <= c):
      medio = b
      mayor = c
  else:
      medio = c
      mayor = b
elif((b <= a) and (b <= c)):
    menor = b;
    if(a <= c):
      medio = a
      mayor = c
    else:
      medio = c
      mayor = a
else:
    menor = c;
    if(a <= b):
      medio = a
      mayor = b
    else:
      medio = b
      mayor = a
print("{},{},{}".format(menor, medio, mayor))