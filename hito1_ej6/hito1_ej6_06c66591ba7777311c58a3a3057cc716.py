#Ordenar tres números
a = int(input('escribe el primer numero:'))
b = int(input('escribe el segundo numero:'))        
c = int(input('escribe el tercer numero:'))

i = min(a,b,c)
r = max(a,b,c)
t = (a + b + c) - i - r

print('{}, {}, {}'.format(i,t,r))