#Entrada
a=int(input("Digitar primer numero: "))
b=int(input("Digitar segundo numero: "))
c=int(input("Digitar tercer numero: "))

#Proceso
if a > b and a > c:
    num_mayor = a
    if b > c:
        num_medio= b
        num_menor= c
    else:
        num_medio= c
        num_menor= b
elif b > a and b >c:
    num_mayor = b
    if a > c:
        num_medio= a
        num_menor= c
    else:
        num_medio= c
        num_menor= a
elif c > a and c >b:
    num_mayor = c
    if b > a:
        num_medio= b
        num_menor= a
    else:
        num_medio= a
        num_menor= b
#Salida
print("{},{},{}".format(num_menor,num_medio,num_mayor))