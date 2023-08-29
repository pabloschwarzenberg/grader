#ordenar tres numeros
a = eval(input('ingrese numero:'))
b = eval(input('ingrese numero:'))
c = eval(input('ingrese numero:'))

if a <= b <= c:
    print('los numeros de menor a mayor son:',a,',',b,',',c)
if a <= c <= b:
    print('los numeros de menor a mayor son:',a,',',c,',',b)
if b <= a <= c:
    print('los numeros de menor a mayor son:',b,',',a,',',c)
if b <= c <= a:
    print('los numeros de menor a mayor son:',b,',',c,',',a)
if c <= a <= b:
    print('los numeros de menor a mayor son:',c,',',a,',',b)
if c <= b <= a:
    print('los numeros de menor a mayor son:',c,',',b,',',a)