# completa el código de la función
def suma_divisores(a):
    divisor=1
    sumaDivisores=0
    while divisor<a:
        if a%divisor==0:
            sumaDivisores=sumaDivisores+divisor
            print('sumaDivisores: ',sumaDivisores)

        divisor=divisor+1
        print('contador: ',divisor)

        if sumaDivisores==1:
            return (sumaDivisores,True)
        else:
            return (sumaDivisores,False)
            
            
 