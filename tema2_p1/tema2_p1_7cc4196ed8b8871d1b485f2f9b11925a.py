def es_primo(num1):
    if num1 > 1:
      n = 0
      m = 2

      while m < num1:
        s = num1 % m
        if s == 0:
            n += 1
            m += 1

        if n == 0:
            return True
        else:
            return False
    else:
        return False


try:
    x = int(input("Ingrese un número: "))
    print(es_primo(x))

except:
    print("Ingrese solo un numero")




