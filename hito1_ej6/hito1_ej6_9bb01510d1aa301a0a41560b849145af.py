x1 = eval(input('ingresa el primer numero:'))
x2 = eval(input('ingresa el segundo numero numero:'))
x3 = eval(input('ingresa uel tercer numero:'))




if x1 <= x2 <= x3 :
    print('El orden es', x1,',',x2,',',x3)
if x3 <= x1 <= x2 :
    print('El orden es', x3,',',x1,',',x2)
if x2 <= x3 <= x1 :
    print('El orden es', x2,',',x3,',',x1)
if x1 <= x3 <= x2 :
    print('El orden es', x1,',',x3,',',x2)
if x3 <= x2 <= x1 :
    print('El orden es', x3,',',x2,',',x1)
if x2 <= x1 <= x3 :
    print('El orden es', x2,',',x1,',',x3)

