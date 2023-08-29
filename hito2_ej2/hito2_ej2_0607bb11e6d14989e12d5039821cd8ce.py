def ValidarAdn(Secuencia):
    Correcta=True
    for i in Secuencia:
        if i=="A" or i=="T" or i=="G" or i=="C" or i=="a" or i=="t" or i=="g" or i=="c":
            pass
        else:
            Correcta=False
            break
    if Correcta:
        print("Secuencia correcta")
    else:
        print('Secuencia incorrecta')
ValidarAdn(input("Ingresa una secuencia "))