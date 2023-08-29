import os
fono1=000
fono2=000
fono3=000
hora=0
correcto=1
continuar=1
while continuar==1:
    while correcto==1:
        fono1=int(input('''Ingrese los 3 primeros numeros del telefono: 
        ''' ))
        fono2=int(input('''Ingrese los 3 siguientes numeros del telefono: 
        ''' ))
        fono3=int(input(''Ingrese los 3 ultimos numeros del telefono: 
        '' ))
        print("fono= {fono1}-{fono2}-{fono3}")
        correcto=int('''Confrimacion:
        /Ingrese 0 si el numero ingresado es correcto/Ingrese 1 si el numero ingresado es incorrecto/''')
    while hora<0 or hora>23:
        os.system("cls")
        hora=input("Ingresar de 0 a 23 para la hora de llegada de la llamada: ")

        os.system("cls")
        print('''Numero: {fono1}{fono2}{fono3}
        Hora:{hora}:00''')
        if 0>hora<7:
            print("Contestar! puede ser emergencia")
        elif hora<14 and fono3!=909:
            print("Resultado: NO CONTESTAR")
        elif 17>hora<19:
            print("Contestar")
        else:
            print("Resultado: NO CONTESTAR")
        os.system("pause")
        os.system("cls")
        continuar=int("Ingrese 1 para realizar otra consulta, 0 para cerrar")