#Ordenar tres números
numero1=eval(input('ingrese un numero:'))
numero2=eval(input('Ingrese un numero:'))
numero3=eval(input('Ingrese un numero:'))

if ((numero1>=numero2) and (numero1>= numero3)and (numero2>=numero3)):
    print(numero3, ',', numero2,',', numero1)

if ((numero1>=numero2) and (numero1>= numero3)and (numero3>=numero2)):
    print(numero2, ',', numero3,',', numero1)

if ((numero2>=numero1) and (numero2>= numero3)and (numero1>=numero3)):
    print(numero3, ',', numero1,',', numero2)

if ((numero2>=numero1) and (numero2>= numero3)and (numero3>=numero1)):
    print(numero1, ',', numero3,',', numero2)
    
if ((numero3>=numero1) and (numero3>= numero2)and (numero2>=numero1)):
    print(numero1, ',', numero2,',', numero3)
    
if ((numero3>=numero1) and (numero3>= numero2)and (numero1>=numero2)):
    print(numero2, ',', numero1,',', numero3)
    
