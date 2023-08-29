#Ordenar tres números
ln = []
orden = ['primer', 'segundo', 'tercer']
on = 0
c = 3
while c > 0:
    ln.append(int(input('Introduzca el {} número entero: '.format(orden[on]))))
    c -= 1
    on += 1
ln.sort()
numor = ','.join(str(num) for num in ln)
print(numor)
