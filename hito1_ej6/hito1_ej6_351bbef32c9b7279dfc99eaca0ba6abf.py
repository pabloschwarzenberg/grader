x = eval(input('Ingrese el primer numero: '))
y = eval(input('Ingrese el segundo numero: '))
z = eval(input('Ingrese el tecer numero: '))

if x <= y <= z:
    print(x ,',',y,',' ,z)
else:
    if x <= z <= y:
        print(x ,',' ,z ,',' ,y)
    else:
        if y <= x <= z:
            print(y ,',' ,x , ',' ,z)
        else:
            if y <= z <= x:
                print(y ,',' ,z ,',' ,x)
            else:
                if z <= x <= y:
                    print(z ,',',x ,',' ,y)
                else:
                    if z <= y <= x:
                        print(z ,',' ,y ,',' ,x)