#Conversión de Decimal a Binario
def binario(numero):
    if numero==0:
        return '0'
    elif numero<0:
        return '-'+binario(-numero)
    else:
        bits=[]
        while numero>0:
            bits.append(str(numero%2))
            numero//=2
        bits.reverse()
        return''.join(bits)
numero_decimal=int(input("Ingrese un número decimal: "))
resultadobi=binario(numero_decimal)
print("Resultado=", resultadobi)
#Fin      