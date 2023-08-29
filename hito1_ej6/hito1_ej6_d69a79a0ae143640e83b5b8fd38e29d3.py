n1=int(input("ingrese un numero"))
n2=int(input("ingrese un numero"))
n3=int(input("ingrese un numero"))
me = 0
ma = 0

if n1 <= n3 and n1 <= n2:
        me = n1
elif n2 <= n3 and n2 <= n1:
        me= n2
elif n3 <= n1 and n3 <= n2:
        me= n3

if n1 >= n3 and n1 >= n2:
        ma = n1
elif n2 >= n3 and n2 >= n1:
        ma= n2
elif n3 >= n1 and n3 >= n2:
        ma= n3


medio = (n1+n2+n3) -(ma + me)
print("los numeros ordenados son : {}, {}, {}".format(me, medio, ma)) 