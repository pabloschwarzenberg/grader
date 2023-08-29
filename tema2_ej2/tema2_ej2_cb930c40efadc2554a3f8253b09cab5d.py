# completa el código de la función
def son_amigos(a, b):
    def suma_divisores(num):
        if num==1:
            suma=1
            return suma
        else:
            suma=0
            for i in range(1, num-1):
                if num%i==0:
                    suma+=i
            return suma
    suma_a=suma_divisores(a)
    suma_b=suma_divisores(b)
    if suma_a==suma_b:
        return True
    else:
        return False
numero_a=1
numero_b=2
