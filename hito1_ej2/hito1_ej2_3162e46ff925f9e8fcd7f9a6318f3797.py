NumTel=eval(input('Ingrese Numero Telefonico de 8 digitos:\t'))
Hora=eval(input('Ingrese Hora de LLamada:\t'))
EsInt=type(NumTel)
esNumVal=NumTel/(10000000)
PruebaLogica = (0<esNumVal<10) and (EsInt==int) and (0<=Hora<=23)
#print(PruebaLogica)
#a=type(TexNumTel)
#print(a, TexNumTel)
while True:
    Ult3Num=str(NumTel)[5:8]
    Pri3Num=str(NumTel)[1:3]
    if PruebaLogica is True:
        if 0<=Hora<=7:
            print('CONTESTAR')
            break
        elif 7<Hora<=14 and Ult3Num!='909':
            print('NO CONTESTAR')
            break
        elif 7<Hora<=14 and Ult3Num=='909':
            print('CONTESTAR')
            break
        elif 17<Hora<19 and Pri3Num!='877':
            print('NO CONTESTAR')
            break
        elif 17<Hora<19 and Pri3Num=='877':
            print('CONTESTAR')
            break
        elif Hora>=19:
            print('NO CONTESTAR')
            break
        else:
            break
    else:
        print('INFORMACIÓN INVALIDA')
        break
print('--FIN--')