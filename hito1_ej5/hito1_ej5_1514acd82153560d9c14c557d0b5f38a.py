rut = [] 

datos = [rut.append(numeros) for numeros in input('RUT ::>')]

rut.reverse()

serie = 2 
multiplicador = 0

"Se procede a tomar el número de RUT de derecha a izquierda, multiplicando cada dígito por los números que componen" \
" la serie numérica 2, 3, 4, 5, 6, y 7; y sumando el resultado de estos productos. Si se ha aplicado la serie hasta" \
" el final y quedan dígitos por multiplicar, se comienza la serie nuevamente:"


for x in rut:
    multiplicador+=int(x)*serie
    if serie==7: serie = 1
    serie+=1
    modulo = multiplicador%11
    resultado = 11-modulo
    if resultado == 11: digito=0 
    elif resultado == 10: digito="K" 
    else: digito=resultado 

print ("dv=",digito)