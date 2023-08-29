#Descomponer un número
num=int(input("INGRESE UN NUMERO DE 4 DIGITOS: "))
while not (num>=0 and num<=9999):
    num=int(input("INGRESE UN NUMERO DE 4 DIGITOS: "))
if num>=0 and num<=9:
    numero=str(num)
    descomposicionunidades=num[0]+"U"
    print(descomposicionunidades)
elif num>=10 and num<=99:
    numero=str(num)
    descomposiciondecena=numero[0]+"D"
    descomposicionunidades=numero[1]+"U"
    print(descomposiciondecena,"+",descomposicionunidades)
elif num>=100 and num<=999:
    numero=str(num)
    descomposicioncentena=numero[0]+"C"
    descomposiciondecena=numero[1]+"D"
    descomposicionunidades=numero[2]+"U"
    print(descomposicioncentena,"+",descomposiciondecena,"+",descomposicionunidades)
elif num>=1000 and num<=9999:
    numero=str(num)
    descomposicionmil=numero[0]+"M"
    descomposicioncentena=numero[1]+"C"
    descomposiciondecena=numero[2]+"D"
    descomposicionunidades=numero[3]+"U"
    print(descomposicionmil,"+",descomposicioncentena,"+",descomposiciondecena,"+",descomposicionunidades)  