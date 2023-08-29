#ENTRADA

def numero_perfecto(p):
    divisor = []
    for variante in range(1, p):
        if p % variante == 0:
            variante = divisor.append(variante)
            
#PROCESAMIENTO

        
    adicion = 0
    for division in divisor:
        adicion = adicion + division
        
    if adicion == p:
        valorpreciso = True
        adicion = 0
        
    else:
        valorpreciso = False
        adicion = 0
        
    return valorpreciso
    
#SALIDA

if __name__=="__main__":
    valor = eval(input("Inserte un valor: "))
    print(valorideal(valor))