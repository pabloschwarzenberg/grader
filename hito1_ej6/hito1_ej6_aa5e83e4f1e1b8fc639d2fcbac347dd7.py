x = int(input('Ingresa primer entero: '))
y = int(input('Ingresa segundo entero: '))
z = int(input('Ingresa tercer entero: '))

if x<=z<=y:
    print(x,',',z,',',y)
else:
    if x<=y<=z:
        print(x,',',y, ',',z)
    
if z<=x<=y:
    print(z,',',x,',',y)
else:
    if z<=y<=x:
        print(z,',',y,',',x)
    
if y<=x<=z:
    print(y,',',x,',',z)
else :
    if y<=z<=x:
        print(y,',',z,',',x)