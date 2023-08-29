def validar_secuencia(secuencia):
    secuencia=secuencia.lower()
    for i in secuencia:
        if i!="a" or i!="c" or i!="t" or i!="g":
            print("La secuencia {0} es incorrecta".format(secuencia))
        else:
            print("La secuencia {0} es correcta".format(secuencia))
            

a=input("Ingrese secuencia: ")
validar_secuencia(a)