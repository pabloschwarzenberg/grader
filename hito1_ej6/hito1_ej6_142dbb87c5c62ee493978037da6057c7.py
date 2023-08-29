numero1 = eval(input('ingresa el primer numero'))
numero2 = eval(input('ingresa el segundo numero'))
numero3 = eval(input('ingresa el tercer numero'))

if numero1 <= numero2 <= numero3:
    print('el orden es:' , numero1  ,',', numero2 ,',', numero3)
if numero1 <= numero3 <= numero2:
    print('el orden es:' , numero1 ,',', numero3 ,',', numero2)
if numero2 <= numero1 <= numero3:
    print('el orden es:' , numero2 ,',', numero1 ,',', numero3)
if numero2 <= numero3 <= numero1:
    print('el orden es:' , numero2 ,',', numero3 ,',', numero1)
if numero3 <= numero1 <= numero2:
    print('el orden es:' , numero3 ,',', numero1 ,',', numero2)
if numero3 <= numero2 <= numero1:
    print('el orden es:' , numero3 ,',', numero2 ,',', numero1)

