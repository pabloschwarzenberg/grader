#Ordenar tres números
print('Ingrese tres numeros enteros')
a=int(input('Ingresa el primer numero:'))
b=int(input('Ingresa el segundo numero:'))
c=int(input('Ingresa el tercer numero:'))
if a>=b>=c:
    print(c,',',b,',',a)
if b>=a>=c:
    print(c,',',a,',',b)
if a>=c>=b:
    print(b,',',c,',',a)
if c>=b>=a:
    print(a,',',b,',',c)
if b>=c>=a:
    print(a,',',c,',',b)
if c>=a>=b:
    print(b,',',a,',',c)