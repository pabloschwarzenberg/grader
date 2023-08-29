celular = 0
hora = ""
bandera = True

print("bienvenido a la contestadora automatica")

while(bandera): 
    celular = int(input("ingrese el numero de celular\n"))
    
    hora = int(input("Ingrese la hora\n"))
    if(len(str(celular)) < 8) or (len(str(celular)) > 8):
        print("El numero de celular tiene que ser de 8 digitos")
        break
    elif(hora >= 0 and hora <= 7):
        print("CONTESTAR")
        break
    elif(hora < 14 and hora > 7):
        ultimosDigitos = str(celular)[5:8]
        if(ultimosDigitos == "909"):
            print("CONTESTAR")
            break
        else:
            print("NO CONTESTAR")
            break
    elif(hora >= 17 and hora <= 19):
        primerosDigitos = str(celular)[0:3]
        if(primerosDigitos == "877"):
            print("NO CONTESTAR")
            break
        else:
            print("CONTESTAR")
            break
    elif(hora > 19):
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")