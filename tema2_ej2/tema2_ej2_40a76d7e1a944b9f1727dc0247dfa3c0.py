"""
Dos números a y b se dicen números amigos, 
si la suma de los divisores de uno de los números es igual al otro número y viceversa 
(en el cálculo de los divisores, no debes considerar al mismo número). 
Crea una función que reciba 2 números, 
y retorne True si es que estos son amigos, y False si es que no lo son.
"""

def amigos(a,b):
    # completa el código de la función

    # amigo A
    contador_a = 0
    print("los divisores de ",a)
    for divisor in range(1,a+1):
        if (a % divisor) == 0 :
            print(divisor,"es divisor")
            contador_a=contador_a+divisor
    print("el numero ",a," la suma de sus divisores es ",contador_a)

    # amigo B
    contador_b= 0
    print("los divisores de ",b)
    for divisor in range(1,b+1):
        if (b % divisor) == 0 :
            print(divisor,"es divisor")
            contador_b=contador_b+divisor
    print("el numero ",b," la suma de sus divisores es ",contador_b)

    if contador_a==contador_b  and a!=b:
        return True
    else:
        return False

if __name__ == "__main__":
    a=int(input("escrriba un numero: "))
    b=int(input("escriba un segundo numero: "))
    print(amigos(a,b))