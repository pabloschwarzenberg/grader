# completa el código de la función
#def amigos(a,b):
#  return
 
def amigos(a ,b):
    suma_a =0
    suma_b =0
    for i in range(1 ,a):
        if a% i == 0:
            suma_a += i

    for k in range(1, b):
        if b % k == 0:
            suma_b += k

    return suma_a == b and suma_b == a



#amigos(220,284)
#a = [220]
#b = [284]
#print(amigos(a,b))
#a = int(input("Ingrese el primer numero: "))
#b = int(input("Ingrese el segundo numero: "))

a = 220
b = 284

if amigos(a,b):
    print("True")
else:
    print("False")