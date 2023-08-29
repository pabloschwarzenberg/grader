n = eval(input("Ingrese un numero de hasta 4 digitos: "))
if n >= 0 and n < 10:
    print(str(n % 10) + "U")
elif n >= 10 and n < 100:
    print(str((n % 100//10)) + "D +", str(n % 10) + "U")
elif n >= 100 and n < 1000:
    print(str((n % 1000)//100) + "C +", str((n % 100)//10) + "D +", str(n % 10) + "U")
elif n >= 1000 and n < 10000:
    print(str(n // 1000) + "M +", str((n % 1000)//100) + "C +", str((n % 100)//10) + "D +", str(n % 10) + "U")
      