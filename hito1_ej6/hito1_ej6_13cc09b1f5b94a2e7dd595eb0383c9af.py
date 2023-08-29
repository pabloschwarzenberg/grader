#Ordenar tres números
nro1 = int(input("Primer Numero:"))
nro2 = int(input("Segundo Numero:"))
nro3 = int(input("Tercer Numero:"))

A = min(nro1,nro2,nro3)
C = max(nro1,nro2,nro3)
B = (nro1 + nro2 +nro3) - A - C

print("los Numeros ordenados son:",(A,B,C))