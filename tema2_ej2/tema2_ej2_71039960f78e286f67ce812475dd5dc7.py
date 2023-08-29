# completa el código de la función
def amigos(num,num2):
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma = suma + i
    

    suma2 = 0 
    for j in range(1,num2):
        if num2 % j  == 0:
            suma2 = suma2 + j
    
    if suma == num2 and suma2 == num:
        return True
    else:
        return False


if __name__== "__main__":
    numero1 = int(input('Ingresa el primer numero: '))
    numero2 = int(input('Ingresa el segundo numero: '))

    print(amigos(numero1,numero2))