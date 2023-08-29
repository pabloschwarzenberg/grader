#Conversión de Decimal a Binario
def binario(x):
    lista =[]
    while x>0:
        Value_B=int(float(x%2))
        lista.append(Value_B)
        print(lista)
        x=(x-Value_B)/2
    RESULTADO = ""
    for t in lista[::-1]:
        RESULTADO=RESULTADO+str(t)
    return RESULTADO
try:
    a = int(input("INGRESE EL NUMERO A CONVERTIR: "))
    calculo=binario(a)
    print("resultado="+calculo)
except:
    print("INGRESE UN VALOR NUMERICO")