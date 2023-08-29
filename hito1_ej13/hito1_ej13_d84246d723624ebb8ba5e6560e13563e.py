def imp_fac_pri(num):
    primer_primo = 2
    while primer_primo <= num:
        if not (num % primer_primo != 0):
            num /= primer_primo
            print(primer_primo)

        else:
            primer_primo += 1



numero = int(input("Ingrese un numero para calcular factores primos: "))
imp_fac_pri(numero)
