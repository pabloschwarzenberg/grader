#Ordenar tres números
x1=int(input('ingrese primer numero: '))
x2=int(input('ingrese segundo numero: '))
x3=int(input('ingrese tecer numero: '))

if  x1 >= x2 >= x3:
   print(x3,',',x2,',',x1)

elif x1 >= x3 >= x2:
  print(x2,',',x3,',',x1)

elif x2 >= x3 >= x1:
  print(x1,',',x3,',',x2)

elif x2 >= x1 >= x3:
  print(x3,',',x1,',',x2)

elif x3 >= x2 >= x1:
  print(x1,',',x2,',',x3)

elif x3 >= x1 >= x2:
  print(x2,',',x1,',',x3)

print('fin ')


      