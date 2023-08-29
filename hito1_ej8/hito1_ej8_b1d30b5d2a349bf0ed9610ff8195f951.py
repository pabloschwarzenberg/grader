#Descomponer un número
n= input("Ingrese un numero: ")
try:
    n0=int(n)
    n1=str(n0)
    if (0<n0<9999):
        primer_num= n1[0:1]
        segundo_num = n1[1:2]
        tercer_num = n1[2:3]
        cuarto_num = n1[3:4]
        if segundo_num == "":
            print("Tu numero es: ",primer_num +"U")
        elif tercer_num == "":
            print("Tu numero es: ",primer_num +"D +", segundo_num +"U")
        elif cuarto_num == "":
            print("Tu numero es: ",primer_num +"C +", segundo_num +"D +", tercer_num +"U")
        else:     
            print("Tu numero es: ",primer_num +"M +", segundo_num +"C +", tercer_num +"D +", cuarto_num +"U")
        
    else:
        print("Ingreselo nuevamente")
except ValueError:
    print("Ingresar solo numeros")