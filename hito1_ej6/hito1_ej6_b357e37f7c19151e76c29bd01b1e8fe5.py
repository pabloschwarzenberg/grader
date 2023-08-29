#Ordenar tres números
numero_1=int(input('ingrese el primer numero                '))
numero_2=int(input('ingrese el segundo numero               '))
numero_3=int(input('ingrese el tercer numero                '))


if numero_1<numero_2<numero_3 or numero_2==numero_1<numero_3:
    print (numero_1,',',numero_2,',', numero_3)

if numero_2<numero_1<numero_3:
    print (numero_2,',',numero_1,',',numero_3)

if numero_2<numero_3<numero_1 or numero_3==numero_2<numero_1:
    print (numero_2,',',numero_3,',',numero_1)

if numero_3<numero_2<numero_1:
    print(numero_3,',',numero_2,',',numero_1)

if numero_3<numero_1<numero_2 or numero_1==numero_3<numero_2:
    print (numero_3,',',numero_1,',',numero_2)

if numero_1<numero_3<numero_2:
    print(numero_1,',',numero_3,',',numero_2)

if numero_1<numero_2==numero_3:
    print (numero_1,',',numero_2,',',numero_3)
if numero_2<numero_1==numero_3:
    print(numero_2,',',numero_3,',',numero_1)
if numero_3<numero_1==numero_2:
    print(numero_3,',',numero_1,',',numero_2)


if numero_1==numero_2==numero_3:
    print ('los numeros son iguales, intentelo otra vez')