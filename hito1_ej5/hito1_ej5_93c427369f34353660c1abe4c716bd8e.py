numeros= (input("Inserte su rut por favor sin digito verificador: "))
nuevo_numero = (numeros[::-1])
if len(nuevo_numero) == 8:
    resultado = (eval(nuevo_numero[0]) * 2 +
                 eval(nuevo_numero[1]) * 3 +
                 eval(nuevo_numero[2]) * 4 +
                 eval(nuevo_numero[3]) * 5 +
                 eval(nuevo_numero[4]) * 6 +
                 eval(nuevo_numero[5]) * 7 +
                 eval(nuevo_numero[6]) * 2 +
                 eval(nuevo_numero[7]) * 3)
else:
    resultado = (eval(nuevo_numero[0]) * 2 +
                 eval(nuevo_numero[1]) * 3 +
                 eval(nuevo_numero[2]) * 4 +
                 eval(nuevo_numero[3]) * 5 +
                 eval(nuevo_numero[4]) * 6 +
                 eval(nuevo_numero[5]) * 7 +
                 eval(nuevo_numero[6]) * 2)


resultado2 = (resultado//11)*11
resultado3 = resultado - resultado2
resultado4 = 11 - resultado3
if resultado4 == 10:
    print("dv=K")
elif resultado4 ==11:
    print("dv=0")
else:
    print("dv="+str(resultado4))
      