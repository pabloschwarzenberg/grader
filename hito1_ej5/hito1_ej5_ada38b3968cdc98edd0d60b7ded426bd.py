#entrada
rut = int(input("Ingrese Su run Sin El digito Verificador: "))
digito_8 = rut % 10
digito_7 = rut %100//10
digito_6 = rut %10**3//100
digito_5 = rut %10**4//10**3
digito_4 = rut %10**5//10**4
digito_3 = rut %10**6//10**5
digito_2 = rut %10**7//10**6
digito_1 = rut %10**8//10**7
#proceso
digito_1 = int(digito_1) * 3
digito_2 = int(digito_2) * 2
digito_3 = int(digito_3) * 7
digito_4 = int(digito_4) * 6
digito_5 = int(digito_5) * 5
digito_6 = int(digito_6) * 4
digito_7 = int(digito_7) * 3
digito_8 = int(digito_8) * 2
#Proceso 2
modulo = (digito_1 + digito_2 + digito_3 + digito_4 + digito_5 + digito_6 + digito_7 + digito_8)%11
digito_verificador = int( 11 - modulo) 
#salida
if digito_verificador == 10:
    print("dv=K")
elif digito_verificador == 11:
    print("dv=0")
else:
    print("dv=",digito_verificador)
