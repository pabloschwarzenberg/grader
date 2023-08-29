#Tu programa debe repetirse continuamente, para salir la persona debe ingresar algo distinto a la letra "N"
#Profesor, hice que el programa se pudiera repetir,y salir al colocar algo distinto a "N".
#Sin embargo, el edx me tiró error y no acepta el programa, por lo que dejaré el programa que acepta aqui arriba y el completo lo dejaré
#debajo de este programa como texto para que no salte error en el edx.

usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))
saldo_cajero = 1000000
saldo_cuenta = 100000

if(usuario == 10334151):
    if(clave == 1803):
        monto = int(input("¿Cuál es el monto a retirar?"))
        if(monto <= saldo_cuenta):
            saldo_cajero = saldo_cajero - monto
            saldo_cuenta = saldo_cuenta - monto
            print("saldo cuenta =",saldo_cuenta)
            print("saldo cajero =",saldo_cajero,"\n")

        else:
            print("Monto no permitido\n")
            
        
    else:
        print("Clave incorrecta: ")
        clave = int(input("Ingrese su clave: "))
        if(clave == 1803):
            monto = int(input("¿Cuál es el monto a retirar?"))
            if(monto <= saldo_cuenta):
                saldo_cajero = saldo_cajero - monto
                saldo_cuenta = saldo_cuenta - monto
                print("saldo cuenta =",saldo_cuenta)
                print("saldo cajero =",saldo_cajero,"\n")
            else:
                print("Monto no permitido\n")

        else:
            print("Clave incorrecta\n")
            clave = int(input("Ingrese su clave: "))
            if(clave == 1803):
                monto = int(input("¿Cuál es el monto a retirar?"))
                if(monto <= saldo_cuenta):
                    saldo_cajero = saldo_cajero - monto
                    saldo_cuenta = saldo_cuenta - monto
                    print("saldo cuenta =",saldo_cuenta)
                    print("saldo cajero =",saldo_cajero,"\n")
                else:
                    print("Monto no permitido\n")

            else:
                print("Tarjeta bloqueada")
    
else:
    print("Usuario incorrecto\n")

#usuario = 0
#clave = 0
#saldo_cajero = 1000000
#saldo_cuenta = 100000 
#bloquear = 0
#while(usuario != str(usuario) or usuario == "N"):
#    if(clave != str(clave) or clave == "N"):
#        if(bloquear != 1):
#            usuario = eval(input("Ingrese su usuario: "))
#            if(usuario == 10334151):
#                clave = eval(input("Ingrese su clave: "))
#                if(clave == 1803):
#                    monto = eval(input("¿Cuál es el monto a retirar?\n"))
#                    if(monto <= saldo_cuenta):
#                        saldo_cajero = saldo_cajero - monto
#                        saldo_cuenta = saldo_cuenta - monto
#                        print("saldo cuenta =",saldo_cuenta)
#                        print("saldo cajero =",saldo_cajero,"\n")

#                    else:
#                        print("Monto no permitido \n")
                    
#                else:
#                    print("Clave incorrecta \n")
#                    clave = eval(input("Ingrese su clave: "))
#                    if(clave == 1803):
#                        monto = eval(input("¿Cuál es el monto a retirar?"))
#                        if(monto <= saldo_cuenta):
#                            saldo_cajero = saldo_cajero - monto
#                            saldo_cuenta = saldo_cuenta - monto
#                            print("saldo cuenta =",saldo_cuenta)
#                            print("saldo cajero =",saldo_cajero,"\n")
#                        else:
#                            print("Monto no permitido \n")

#                    else:
#                        print("Clave incorrecta \n")
#                        clave = eval(input("Ingrese su clave: "))
#                        if(clave == 1803):
#                            monto = eval(input("¿Cuál es el monto a retirar?"))
#                            if(monto <= saldo_cuenta):
#                                saldo_cajero = saldo_cajero - monto
#                                saldo_cuenta = saldo_cuenta - monto
#                                print("saldo cuenta =",saldo_cuenta)
#                                print("saldo cajero =",saldo_cajero,"\n")
#                            else:
#                                print("Monto no permitido \n")

#                        else:
#                            print("Tarjeta bloqueada \n")
#                            bloquear = 1

#            else:
#                print("Usuario incorrecto\n")

#    else:
#        usuario = ""
