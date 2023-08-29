n1 = int(input("bienvenido,ingrese el numero 1: "))
n2 = int(input("bienvenido,ingrese el numero 2: "))
n3 = int(input("bienvenido,ingrese el numero 3: "))

if n1<=n2<=n3:
    print ("Los numeros ordenados de mayor a menor son",n1,",",n2,",",n3)

elif n3<=n2<=n1:
    print ("Los numeros ordenados de mayor a menor son",n3,",",n2,",",n1)

elif n2<=n3<=n1:
    print ("Los numeros ordenados de mayor a menor son",n2,",",n3,",",n1)

elif n2<=n1<=n3:
    print ("Los numeros ordenados de mayor a menor son",n2,",",n1,",",n3)

elif n1<=n3<=n2:
    print ("Los numeros ordenados de mayor a menor son",n1,",",n3,",",n2)

elif n3<=n1<=n2:
    print ("Los numeros ordenados de mayor a menor son",n3,",",n1,",",n2)    