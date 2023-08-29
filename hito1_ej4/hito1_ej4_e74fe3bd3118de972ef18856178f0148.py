x = eval(input("Ingrese Número: "))
resultado = bin(x)
if len(resultado) <= 8:   
    a = int(resultado[2:8])
    print("resultado=", a)
if len(resultado) == 9:   
    a = int(resultado[2:9])
    print("resultado=", a)
if len(resultado) == 10:   
    a = int(resultado[2:10])
    print("resultado=", a)