#Descomponer un número
x = int(input('Ingresa un numero de hasta 4 digitos: '))

if 0000 <= x <= 9999:

    ultimoDigito =  x%10
    x = x//10

    digitoDelMedio2= x%10
    x = x//10

    digitoDelMedio = x%10
    x = x//10

    primerDigito = x%10





    print('El numero descompuesto es: ', primerDigito, 'M', '+', digitoDelMedio, 'C', '+' , digitoDelMedio2,'D', '+' , ultimoDigito,'U')