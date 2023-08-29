def ordenro(nro1, nro2, nro3):
    
    if nro1 > nro2:
        nro1, nro2 = nro2, nro1 
    if nro2> nro3:
        nro2 , nro3 = nro3, nro2
    if nro1 > nro2:
        nro1, nro2 = nro2, nro1 
    return nro1, nro2, nro3
    
nro1 = int(input("Ingrese el primer numero: "))
nro2 = int(input("Ingrese el segundo numero: "))
nro3 = int(input("Ingrese el tercer numero: "))

nro1, nro2, nro3 = ordenro (nro1, nro2, nro3)

print("Resultados: {},{},{}".format(nro1,nro2,nro3))