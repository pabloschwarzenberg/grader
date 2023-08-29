print("bienvenido, escoga 3 números enteros que desea ordenar: ")
n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Tercer número: "))
mn = min(n1, n2, n3)
mx = max(n1, n2, n3)
R = (n1 + n2 + n3) - mn - mx 
print("Los números ordenados son los sgte: {}, {}, {}".format(mn,R,mx))
