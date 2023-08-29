#Ordenar tres números
      print('Ingrese 3 números  enteros para que el programa los muestre ordenados de mayor a menor')





x=int(input('Ingrese el primer número: '))
y=int(input('Ingrese el segundo número: '))
z=int(input('Ingrese el tercer número: '))

if x>=y>=z :
    print('El resultado es: ',x,',',y,',',z)
else:
    if x>=z>=y :
        print('El resultado es: ',x,',',z,',',y)
    else:
        if y>=x>=z :
            print('El resultado es: ',y,',',x,',',z)
        else:
            if y>=z>=x :
                print('El resultado es: ',y,',',z,',',x)
            else:
                if z>=x>=y :
                    print('El resultado es: ',z,',',x,',',y)
                else:
                    print('El resultado es: ',z,',',y,',',x)
    
