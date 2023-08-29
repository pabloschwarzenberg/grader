#Ordenar tres números
numero1 = eval(input('Ingrese número 1: '))
numero2 = eval(input('Ingrese número 2: '))
numero3 = eval(input('Ingrese número 3: '))

if numero1<=numero2<=numero3:
     print('los numeros de menor a mayor son: ',numero1,',',numero2,',',numero3)
elif numero1<=numero3<=numero2:
     print('los numeros de menor a mayor son: ',numero1,',',numero3,',',numero2)
elif numero2<=numero1<=numero3:
     print('los numeros de menor a mayor son: ',numero2,',',numero1,',',numero3)
elif numero2<=numero3<=numero1:
     print('los numeros de menor a mayor son: ',numero2,',',numero3,',',numero1)
elif numero3<=numero1<=numero2:
     print('los numeros de menor a mayor son: ',numero3,',',numero1,',',numero2)
elif numero3<=numero2<=numero1:
     print('los numeros de menor a mayor son: ',numero3,',',numero2,',',numero1)

  