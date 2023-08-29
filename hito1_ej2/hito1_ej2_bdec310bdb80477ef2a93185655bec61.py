#Contestador de celular
N = str(input('Ingrese un número telefónico: '))
H = int(input('Ingrese hora de llamada: '))
print('Variable Str: ',N)
a = N[0:3]
print('Los primeros números son: ',a)
b = N[5:8]
print('Los últimos números son: ',b)
c = 877
c = str(c)
print('Variable de inicio tres dígitos: ',c)
d = 909
d = str(d)
print('Variable de termino tres dígitos: ',d)
if 0<= H <= 7:
    print('Contestar')
elif 7 < H < 14:
    if b == d:
        print('Contestar')
    else:
        print('No contestar')
    
elif 14 <= H < 17:
    print('No contestar')
elif 17 <= H <= 19:
    if a == c:
      print('No contestar')
    else:
        print('Contestar')
elif H > 19:
  print('No contestar')
    