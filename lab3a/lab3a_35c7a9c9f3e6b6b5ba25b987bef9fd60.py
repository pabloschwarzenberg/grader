#calculadora
cantidad=0
promedio=0
while True:
    n=int(input('ingresar numeros:'))
    if n==-1:

        break
    cantidad=cantidad+1
    promedio=promedio+n
if cantidad==0:

    print('cantidad=0')
    print('promedio=nd')
    print('minimo=nd')
else:
    promedio=promedio/cantidad        
    print('cantidad=',cantidad)
    print('promedio=',round(promedio,1))
