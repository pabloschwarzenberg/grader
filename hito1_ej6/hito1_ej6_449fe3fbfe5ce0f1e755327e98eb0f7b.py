#Ordenar tres números
print('Escribe tres números enteros y te los ordenaré de menor a mayor')

print('El primero es:')
x=int(input())

print('El segundo es:')
y=int(input())

print('y el tercero es:')
z=int(input())


if x<=y<=z:
    print('Entonces de menor a mayor son',x,',',y,',',z)
else:
    if x<=z<=y:
        print('Entonces de menor a mayor son',x,',',z,',',y)
    else:
        if y<=x<=z:
            print('Entonces de menor a mayor son',y,',',x,',',z)
        else:
            if y<=z<=x:
                print('Entonces de menor a mayor son',y,',',z,',',x)
            else:
                if z<=x<=y:
                    print('Entonces de menor a mayor son',z,',',x,',',y)
                else:
                    print('Entonces de menor a mayor son',z,',',y,',',x)
