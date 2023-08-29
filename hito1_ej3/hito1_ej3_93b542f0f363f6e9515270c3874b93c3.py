#Aprobación de créditos
print("HOLA BUENAS, BIENVENIDO AL BANCO. A CONTINUACION NECESITAREMOS ALGUNOS DATOS")
lucas= int(input("INGRESAR REMUNERACION EN PESOS $: "))
naci= int(input("INGRESAR EL AÑO DE NACIMIENTO: "))
hijos= int(input("INGRESAR NUMEROS DE HIJOS: "))
años= int(input("INGRESAR AÑOS DE ANTIGÜEDAD EN EL BANCO: "))
civil= input("INGRESAR ESTADO CIVIL CASADO 'C' O SOLTERO 'S': ")
resi= input("INGRESAR LUGAR DE RESIDENCIA URBANO 'U' O RURAL 'R' : ")
edad=2020-naci
residencia=resi
estado=civil
if años>10 and hijos>=2:
    print("APROBADO")
elif estado==civil and hijos>3:
    if edad>=45 and edad<=55:
        print("APROBADO")
    else:
        print("RECHAZADO")
elif lucas>2500000 and estado==civil and residencia==resi:
    print("APROBADO")
elif lucas>3500000 and años>5:
    print("APROBADO")
elif residencia==resi and estado==civil and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
