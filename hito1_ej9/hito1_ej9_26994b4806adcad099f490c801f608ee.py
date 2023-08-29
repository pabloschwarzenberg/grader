def sistema_de_ecuaciones():
    print("Resolver sistemas de ecuaciones de la forma ax+by=c")
    a = eval(input("Ingrese la incognita A de la primera ecuación: "))
    b = eval(input("Ingrese la incognita B de la primera ecuación: "))
    c = eval(input("Ingrese la incognita C de la primera ecuación: "))
    d = eval(input("Ingrese la incognita A de la segunda ecuación: "))
    e = eval(input("Ingrese la incognita B de la segunda ecuación: "))
    f = eval(input("Ingrese la incognita C de la segunda ecuación: "))

    matrizcoef = (a) * (e) - (b) * (d)
    matrizX = (c) * (e) - (b) * (f)
    matrizY = (a) * (f) - (c) * (d)

    valorX = round((matrizX / matrizcoef), 1)
    valorY = round((matrizY / matrizcoef), 1)

    print("x=", str(valorX))
    print("y=", str(valorY))
sistema_de_ecuaciones()

