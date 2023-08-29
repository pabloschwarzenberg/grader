def dvRut(rut): #12 345 678
        rut_str = str(rut)
        reverse_rut = rut_str[::-1]
        factor = 2
        suma = 0

        for digit in reverse_rut:
                suma += int(digit) * factor
                factor += 1
                if factor == 8:
                        factor = 2

        digito_verificador = 11 - (suma % 11)
        if digito_verificador == 1:
                digito_verificador = 1
        elif digito_verificador == 2:
                digito_verificador = 2
        elif digito_verificador == 3:
                digito_verificador = 3
        elif digito_verificador == 4:
                digito_verificador = 4
        elif digito_verificador == 5:
                digito_verificador = 5
        elif digito_verificador == 6:
                digito_verificador = 6
        elif digito_verificador == 7:
                digito_verificador = 7
        elif digito_verificador == 8:
                digito_verificador = 8
        elif digito_verificador == 9:
                digito_verificador = 9
        elif digito_verificador == 11:
                digito_verificador = 0
        elif digito_verificador == 10:
                digito_verificador = 'K'

        return digito_verificador


#Solicitar el número de RUT al usuario
rut = int(input('Ingresa el número de RUT sin dígito verificador'))

#Calcular el dígito verificador
dv = dvRut(rut)

#Impirmir el resultado
print("dv=",dv)