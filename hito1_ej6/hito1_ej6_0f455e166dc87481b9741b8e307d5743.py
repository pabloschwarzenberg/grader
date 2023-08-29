# entrada

n1 = int(input("escriba el 1er numero: "))
n2 = int(input("escriba el 2do numero: "))
n3 = int(input("escriba el 3r numero: "))

# procesamiento

if n1 >= n2 >= n3:
    print(n3, ",", n2, ",", n1, sep='')
elif n2 >= n1 >= n3:
    print(n3, ",", n1, ",", n2, sep='')
elif n3 >= n1 >= n2:
    print(n2, ",", n1, ",", n3, sep='')
elif n3 >= n2 >= n1:
    print(n1, ",", n2, ",", n3, sep='')
elif n2 >= n3 >= n1:
    print(n1, ",", n3, ",", n2, sep='')
elif n1 >= n3 >= n2:
    print(n2, ",", n3, ",", n1, sep='')
