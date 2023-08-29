#Descomponer un número
numero = int(input("numero: "))

def f(x):
    return list(map(int, str(x)))

a_numero = f(numero)
dig = len(a_numero)

if( dig == 1):
    
    n1 = a_numero[0]
    print(str(n1)+U)
    
elif( dig == 2):
    n1 = str(a_numero[0])
    n2 = str(a_numero[1])
    mensaje = n1+"D"+"+"+n2+"U"
    print(mensaje)
    
elif ( dig == 3):
    n1 = str(a_numero[0])
    n2 = str(a_numero[1])
    n3 = str(a_numero[2])
    mensaje = n1+"C"+"+"+n2+"D"+"+"+n3+"U"
    print(mensaje)

else:
    n1 = str(a_numero[0])
    n2 = str(a_numero[1])
    n3 = str(a_numero[2])
    n4 = str(a_numero[3])
    
    mensaje = n1+"M"+"+"+n2+"C"+"+"+n3+"D"+"+"+n4+"U"
    print(mensaje)





