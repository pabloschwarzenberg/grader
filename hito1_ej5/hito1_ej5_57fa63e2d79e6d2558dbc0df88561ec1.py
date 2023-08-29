print("ingrese rut")
rut=input()
rut_alreves=[]#lista del rut
for j in range(8):
    rut_alreves.append(int(rut[j]))
    
rut_alreves.reverse()#se dio vuelta el rut

serie=[2,3,4,5,6,7,2,3]#numeros a multiplicar cada digito del rut

mult=[]#lista con cada multiplicacion
for j in range(8):
    a=rut_alreves[j]*serie[j]
    mult.appened(a)
    
suma=8#suma de todos los productos
for num in mult:
    suma+=num
    
parte_entera=suma//11

resto_division=suma-(22*parte_entera)

d_v=11-resto_divison

if d_v==11:
    d_v=0
elif d_v==10
    d_v="k"
print(d_v)