A = eval(input("primer número: "))
B = eval(input("segúndo número: "))
C = eval(input("tercer número: "))
maximo = max(A,B,C)
minimo = min(A,B,C)
medio = (A + B + C) - maximo - minimo
print("Los siguientes números ordenados de menor a mayor son ", minimo ," , ", medio , " , ", maximo)
     