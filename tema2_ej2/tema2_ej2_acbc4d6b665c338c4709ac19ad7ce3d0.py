def son_amigos(a, b):
    def suma_divisores(num):
        suma=0
        for i in range(1, num + 1):
            if num%i==0 and i != num:
                suma+=i
        return suma

    suma_a=suma_divisores(a)
    suma_b=suma_divisores(b)

    if suma_a==b and suma_b==a:
        return True
    else:
        return False

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

if son_amigos(num1, num2):
    print("{} y {} son numeros amigos".format(num1, num2))
else:
    print("{} y {} no son numeros amigos".format(num1, num2))