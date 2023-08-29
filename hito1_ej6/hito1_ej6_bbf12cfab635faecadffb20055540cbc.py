x_1=int(input("Ingrese el primer numero:"))
x_2=int(input("Ingrese el primer numero:"))
x_3=int(input("Ingrese el primer numero:"))
n_mayor= max(x_1, x_2, x_3)
n_menor= min(x_1, x_2, x_3)
n_media= (x_1+x_2+x_3) - n_mayor - n_menor
print("los numeros ordenados de menor a mayor son: {},{},{}".format(n_menor, n_media, n_mayor))