#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut,exeptuando su digito verificador (Sin puntos) : "))
print("A continuacion calcularemos la incognita de su digito verificador")

if 10000000<=rut<=99999999:
    
    pri = rut%10
    seg = (rut//10) %10
    ter = (rut//100) %10
    cua = (rut//1000) %10
    qui = (rut//10000) %10
    sex = (rut//100000) %10
    sep = (rut//1000000) %10
    cho = (rut//10000000) %10

    pri = pri * 2
    seg = seg * 3
    ter = ter * 4
    cua = cua * 5
    qui = qui * 6
    sex = sex * 7
    sep = sep * 2
    cho = cho * 3

    modulo = 11
    productos = (pri + seg + ter + cua + qui + sex + sep + cho)
    pentera = (productos//modulo)
    rde = productos - (modulo * pentera)

    dv = modulo - rde
    
    if dv == 11:
        dv = 0
        print(dv=0)
  
        
    elif dv == 10:
        dv = "K"
        print("dv=k")
        
    else:
        print("dv=",dv)

elif 1000000<=rut<=9999999:
            pri = rut%10
            seg = (rut//10) %10
            ter = (rut//100) %10
            cua = (rut//1000) %10
            qui = (rut//10000) %10
            sex = (rut//100000) %10
            sep = (rut//1000000) %10

            pri = pri * 2
            seg = seg * 3
            ter = ter * 4
            cua = cua * 5
            qui = qui * 6
            sex = sex * 7
            sep = sep * 2

            modulo = 11
            productos = (pri + seg + ter + cua + qui + sex + sep)
            pentera = (productos//modulo)
            rde = productos - (modulo * pentera)

            dv = modulo - rde

            if dv == 11:
                dv = 0
                print("dv=",dv)
  
        
            elif dv == 10:
                dv = "K"
                print("dv=",dv)
        
            else:
                print("dv=",dv)
                