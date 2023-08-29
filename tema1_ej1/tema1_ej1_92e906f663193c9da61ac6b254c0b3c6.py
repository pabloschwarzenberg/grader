#Suma de los N primeros números
while True:
    try:
        n1 = int(input('Ingrese un número natural: '))
    except: 
        print('Respuesta inválida')
        continue
    if n1 < 0:
        print('Respuesta inválida')
        continue
    elif n1 >= 0:
        break
x = n1
y = (x*(x+1))/2
print(int(y))

      