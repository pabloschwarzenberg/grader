#Ordenar tres números
numero1=int(input('ingrese primero numero'))
numero2=int(input('ingrese segundo numero'))
numero3=int(input('ingrese tercer numero'))
if numero1>=numero2 and numero2>numero3:
    print('menor a mayor:',str(numero3),',',str(numero2),',',str(numero1))
    
if numero1>=numero3 and numero3>numero2:
    print('menor a mayor:',str(numero2),',',str(numero3),',',str(numero1))

if numero2>=numero3 and numero3>numero1:
    print('menor a mayor:',str(numero1),',',str(numero3),',',str(numero2))

if numero2>=numero1 and numero1>numero3:
    print('menor a mayor:',str(numero3),',',str(numero1),',',str(numero2))

if numero3>=numero1 and numero1>numero2:
    print('menor a mayor:',str(numero2),',',str(numero1),',',str(numero3))

if numero3>=numero2 and numero2>numero1:
    print('menor a mayor:',str(numero1),',',str(numero2),',',str(numero3))

if numero1==numero2==numero3:
    print('son todos iguales')