print('Ingrese 3 números distintos')

numero1 = eval(input('\nIngresa el primer número: '))
numero2 = eval(input('\nIngresa el segundo número: ')) 
numero3=eval(input('\nIngresa el tercer número: '))

if numero1>=numero2:
   if numero1>=numero3:
       if numero2>=numero3:
           print(numero3,',',numero2,',',numero1)

       else:
           print(numero2,',',numero3,',',numero1)


elif numero2>=numero3:
        if numero2>=numero1:
            if numero1>=numero3:
                print(numero3,',',numero1,',',numero2)
            
            else:
                print(numero1,',',numero3,',',numero2)


elif numero3>=numero1:
        if numero3>=numero2:
            if numero2>=numero1:
                print(numero1,',',numero2,',',numero3)
            
            else:
                print(numero2,',',numero1,',',numero3)

