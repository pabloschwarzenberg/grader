#Ordenar tres números
x = int(input("ingrese numero 1: "))
a = int(input("ingrese numero 2: "))
c = int(input("ingrese numero 3: "))

m = min(x,a,c)
ma = max(x,a,c)
medio = (x + a + c) - ma - m

print("tus numeros oredenados son: {}, {}, {}".format(m, medio, ma))     