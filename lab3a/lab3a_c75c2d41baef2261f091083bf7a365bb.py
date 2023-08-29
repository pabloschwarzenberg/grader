cantidad=0
promedio=0
while True:
    n=float(input('ingrese numeros: '))
    if n==-1:
        print('cantidad=',cantidad)
        print('promedio= nd')
        print('minimo= nd')
        break
    if n>=0:
        promedio=promedio+n
    cantidad=cantidad+1
    promedio=promedio/cantidad
print("cantidad=",cantidad)
print('Promedio: ',round(promedio,1))

