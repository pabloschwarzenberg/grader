rf=int(input("Ingrese el rut sin el mumero identificador"))
digitoverificador3=0

septimoN=int(str(rf)[6])
sextoN=int(str(rf)[5])
quintoN=int(str(rf)[4])
cuartoN=int(str(rf)[3])
tercern=int(str(rf)[2])
segundoN=int(str(rf)[1])
primerN=int(str(rf)[0])

#operaciones
#-------------------------------------------------------------------------------------
n1=primerN*2    
n2=segundoN*7
n3=tercern*6
n4=cuartoN*5
n5=quintoN*4
n6=sextoN*3
n7=septimoN*2


suma=n1+n2+n3+n4+n5+n6+n7

numerodivision=suma/11

division_completa=suma-(11* numerodivision)

digitoverificador=11-division_completa
digitoverificador2=round(digitoverificador)

if digitoverificador2 == 11:
    digitoverificador3=0
elif digitoverificador2 == 10:
    digitoverificador3=int("k")
else :
    digitoverificador3=digitoverificador
print("El digito verificador es :", digitoverificador3)