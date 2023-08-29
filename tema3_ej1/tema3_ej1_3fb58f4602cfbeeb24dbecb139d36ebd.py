# completa el código de la función
def suma_divisores(a):
    suma_a=0
    for i in range(1,a):
        if a % i == 0: 
            suma_a += i
    if(suma_a==1):
       resultado= (int(suma_a), True)
       return resultado
    else:
        resultado1= (int(suma_a), False)
        return resultado1
if __name__ == "__main__":
    h=int(input())
    suma_divisores(h)

           