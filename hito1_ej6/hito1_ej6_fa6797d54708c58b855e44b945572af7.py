#Ordenar tres números
x = eval(input('Escribe tu primer numero: '))
y = eval(input('Escribe tu segundo numero: '))
m = eval(input('Escribe tu tercer numero: '))
if x <= y <= m:
    print('Su orden seria: ', x,',', y,',', m,)
if x <= m <= y:
    print('Su orden seria: ', x,',', m,',', y,)
if m <= y <= x:
    print('Su orden seria: ', m,',', y,',', x,)
if m <= x <= y:
    print('Su orden seria: ', m,',', x,',', y,)
if y <= m <= x:
    print('Su orden seria: ', y,',', m,',', x,)
if y <= x <= m:
    print('Su orden seria: ', y,',', x,',', m,)
