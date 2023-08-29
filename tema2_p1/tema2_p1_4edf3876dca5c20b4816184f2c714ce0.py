# por favor escribe aquí tu función
def app():
    num = int(input('ingrese n: '))

if __name__ == '__main__':
    app()
def  isPrime ( num ):
    if  num  <  1 :
        volver  falso
    elif  num  ==  2 :
        volver  verdadero
    mas :
        para  i  en  rango ( 2 , num ):
            si  num  %  i  ==  0 :
                volver  falso
        volver  verdadero            

 aplicacion def ():
    num  =  int ( input ( 'Escribe un número:' ))
    resultado  =  isPrime ( num )

if  __name__  ==  '__main__' :
    aplicacion ()
def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('Write a number: '))
    result = isPrime(num)

    if result is True:
        print('The number is prime!!')
    else:
        print('The number is not prime!!')

if __name__ == '__main__':
    app()