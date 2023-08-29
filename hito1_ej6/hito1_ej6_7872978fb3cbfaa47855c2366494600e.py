#Ordenar tres números
num_uno = int(input("Primer número: "))
num_dos = int(input("Segundo número: "))
num_tres = int( input("Tercer número: "))

lis = [num_uno, num_dos, num_tres]
lisx = sorted(lis)
menor = str(lisx[0])
medio = str(lisx[1])
mayor = str(lisx[2])

mensaje = menor+","+medio+","+ mayor


print(mensaje)