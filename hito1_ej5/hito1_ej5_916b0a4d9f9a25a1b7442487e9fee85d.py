print("Cálculo del dígito verificador de un rut")
rut=input("Ingrese rut sin puntos ni dígito verificador:")
tamaño=len(rut)
if tamaño==8:
    digito8=int(rut[7])*2
    digito7=int(rut[6])*3
    digito6=int(rut[5])*4
    digito5=int(rut[4])*5
    digito4=int(rut[3])*6
    digito3=int(rut[2])*7
    digito2=int(rut[1])*2
    digito1=int(rut[0])*3
    totalRut=digito8+digito7+digito6+digito5+digito4+digito3+digito2+digito1
    sumaTotal=int(totalRut/11)
    valorTotal=totalRut-(sumaTotal*11)
    digitoVerificador=11-valorTotal
    if digitoVerificador==10:
        digitoVerificador="k"
    if digitoVerificador==11:
        digitoVerificador=0
    print("dv=",digitoVerificador)
if tamaño==7:
    digito7=int(rut[6])*2
    digito6=int(rut[5])*3
    digito5=int(rut[4])*4
    digito4=int(rut[3])*5
    digito3=int(rut[2])*6
    digito2=int(rut[1])*7
    digito1=int(rut[0])*2
    totalRut=digito7+digito6+digito5+digito4+digito3+digito2+digito1
    sumaTotal=int(totalRut/11)
    valorTotal=totalRut-(sumaTotal*11)
    digitoVerificador=11-valorTotal
    if digitoVerificador==10:
        digitoVerificador="k"
    if digitoVerificador==11:
        digitoVerificador=0
    print("dv=",digitoVerificador)