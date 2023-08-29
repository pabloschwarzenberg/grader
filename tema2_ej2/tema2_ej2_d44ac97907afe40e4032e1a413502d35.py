# completa el código de la función
def amigos(a,b):
    totalDeA = 0
    totalDeB = 0
    dividiendo = 1
    suma = 0
    while dividiendo != a+1:
        
        if a/dividiendo == round(a/dividiendo) or a/dividiendo == round(a/dividiendo) +1:
            suma = suma + dividiendo
        suma = suma + a
        totalDeA = suma
    suma = 0
    dividiendo = 1
    while dividiendo != b+1:
        
        if b/dividiendo == round(b/dividiendo) or b/dividiendo == round(b/dividiendo) +1:
            suma = suma + dividiendo
        suma = suma + b
        totalDeB = suma
    if totalDeA == totalDeB:
        return True
     
    return False

print(amigos(11,11))