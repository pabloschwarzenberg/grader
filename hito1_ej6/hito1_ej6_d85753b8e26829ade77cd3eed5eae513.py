h = int(input('escriba el primer numero:  '))
y = int(input('escriba el segundo numero: '))
l = int(input('escriba el tercer numero:  '))

a = min(h, y, l)
c = max(h,y,l)
b = (h + y + l) - a - c

print('los numeros ordenados son:{}, {} , {}'.format(a,b,c))