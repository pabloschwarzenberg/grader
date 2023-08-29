r=0
while r==0:

    numero=input("Introduce un número a descomponer(max 9999): ")

    numero = int(numero)
    variable = str(numero)

    len(variable)



    if len(variable)>4:
        print("El número ingresado no es valido, por favor pruebe con otro")

    else:
        mil=numero/1000
        tmp=numero%1000

        cien=tmp/100
        tmp=tmp%100

        diez = tmp / 10
        tmp = tmp % 10

        uno=tmp/1 
        tmp=tmp%1

    if len(variable)==1:
        valor=str(int(uno))+"U"
        uno = int(uno)
        print(w)
        r=1

    if len(variable)==2:
        valor=str(int(diez))+"D+"+str(int(uno))+"U"
        print(valor)
        r=1

    if len(variable)==3:
        valor=str(int(cien))+"C+"+str(int(diez))+"D+"+str(int(uno))+"U"
        print(valor)
        r=1

    if len(variable)==4:
        valor=str(int(mil))+"M+"+str(int(cien))+"C+"+str(int(diez))+"D+"+str(int(uno))+"U"
        print(valor)
        r=1