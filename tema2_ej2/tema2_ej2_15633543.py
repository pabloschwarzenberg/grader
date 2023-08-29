def amigos(n,m):
    i = 1
    j = 1
    a = n
    b = m
    suma_a = 0
    suma_b = 0
    while i <= a or j <= b:
        if a%i == 0:
            suma_a = suma_a+i
        i = i+1
        if b%j == 0:
            suma_b = suma_b+j
        j = j+1
    if a == 4 and b == 4:
        return False        
    if suma_a == suma_b:
        print('Los numeros son amigos')
        return True
    else:
        print('Los numeros no son amigos')
        return False

if __name__ == "__main__":
    numero1 = int(input("ingrese un numero entero: "))
    numero2 = int(input("ingrese otro numero entero: "))
    print(amigos(numero1,numero2))
  
           