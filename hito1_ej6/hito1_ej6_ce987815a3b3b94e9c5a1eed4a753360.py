#Ordenar tres números
x = eval(input('Ingrese primer número: '))
y = eval(input('Ingrese segundo número: '))
z = eval(input('Ingrese tercer número: '))

x = str(x)
y = str(y)
z = str(z)

if x <= y <= z:
    print('El orden de menor a mayor es: '+x+','+y+','+z)
else:
    if x <= z <= y:
        print('El orden de menor a mayor es: '+x+','+z+','+y)
    else:
        if y <= z <= x:
            print('El orden de menor a mayor es: '+y+','+z+','+x)
        else:
            if y <= x <= z:
                print('El orden de menor a mayor es: '+y+','+x+','+z)
            else:
                if z <= x <= y:
                    print('El orden de menor a mayor es: '+z+','+x+','+y)
                else:
                    if z <= y <= x:
                        print('El orden de menor a mayor es: '+z+','+y+','+x)
