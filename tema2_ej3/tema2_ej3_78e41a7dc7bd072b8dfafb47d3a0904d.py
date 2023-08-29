# Numeros Perfectos

def numero_perfecto(a):
    divisores=[]
    if a < 1:
        print("Error: el numero ingresado es inválido")
    else:
        # para buscar el divisor desde el 1 al numero
        for i in range(1, a + 1):
            # si la division es exacta, significa que es divisor
            if a%i==0:
                divisores.append(i)
        # para sumar los divisores almacenados
        suma=0
        for i in range(0, len(divisores)-1):
            suma=suma+divisores[i]
            i+=1
        if suma == a:
            return True
        else:
            return False

if __name__=="__main__":
    num=int(input("Ingrese un número: "))
    print(numero_perfecto(num))
           