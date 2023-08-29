#Cálculo del dígito verificador de un rut
def CalculoDV(rut): #funcion con un solo input que sea rut
    digitos=[int(d) for d in rut[::-1]] # transforma el input en una lista invertida para el calculo
    suma=sum(d*(2+i % 6) for i, d in enumerate(digitos))
    resto=suma % 11 # el resto es igual a lo restante de "suma" dividido en 11 si no se transforma en decimales
    if(resto==0):
        DV="0"
        return DV
    elif(resto==1):
        DV="K"
        return DV
    else:
        DV=str(11-resto) # se prepara en un string la operación 11-resto
        return DV

rut=input("Ingrese el RUT sin dígito verificador ni puntos: ")

CalculoDV_Resultado = CalculoDV(rut)
print("dv=",CalculoDV_Resultado)