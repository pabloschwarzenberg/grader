#Cálculo del dígito verificador de un rut
#Definir la funcion digito_verificador
def digito_verificador(rut):
    rut=str(rut)
    rut_alreves= rut[::-1]

    multiplicador=2
    suma=0
    #Se recorre los digitos del rut alreves y se realiza la multiplicacion correspondiente
    for digito in rut_alreves:
        suma=suma+(int(digito)*multiplicador)
        multiplicador=multiplicador+1
        #Si el multiplicador es mayor a 7 el multiplicador=2
        if multiplicador>7:
            multiplicador=2
    #Calcular el digito verificador
    dV=11-(suma%11)
    #Si el resultado es 11, el digito verificador=0
    if dV==11:
        return 0
    #Si el resultado es 10, el digito verificador=K
    elif dV==10:
        return 'K'
    else:
        return dV

#Pedir al usuario ingresar su rut sin divito verificador 
rut=input("Ingrese su rut sin digito verificador: ")

dV=digito_verificador(rut)

print("dV= ",dV)      