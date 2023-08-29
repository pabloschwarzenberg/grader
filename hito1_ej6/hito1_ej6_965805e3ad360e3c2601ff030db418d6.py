#ordenar numeros ingreasados
#de menor a mayor
a = input("ingrese su primer valor: ")
b = input("ingrese su segundo valor: ")
c = input("ingrese su tercer valor: ")
#en caso de que ingresemos una letra nos arrogaria error
#la condicion tiene que estar dentro de Try para que acoja a todos los casos
try:
    a = int(a)
    b = int(b)
    c = int(c)
    #agregamos los condicionales
    #todos los casos que nos pueden dar las 3 variables
    if a > b and a > c:
        if b > c: 
            print("el orderden de los numeros que ingreso es" , str(c) + "," + str(b) + "," + str(a))
        else:
            print("el orderden de los numeros que ingreso es" , str(b) + "," + str(c) + "," + str(a))
    elif b > a and b > c:
        if a > c:
            print("el orderden de los numeros que ingreso es" , str(c) + "," + str(a) + "," + str(b))
        else: 
            print("el orderden de los numeros que ingreso es" , str(a) + "," + str(c) + "," + str(b))
    elif c > a and c > b:
        if a > b:
            print("el orderden de los numeros que ingreso es" , str(b) + "," + str(a) + "," + str(c)) 
        else: 
            print("el orderden de los numeros que ingreso es" , str(a) + "," + str(b) + "," + str(c))
except ValueError:
    print("no es un numero")


