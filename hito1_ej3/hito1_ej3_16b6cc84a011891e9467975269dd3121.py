S=1
C=2
U=3
R=4

ingresos=eval(input('ingresos en pesos: '))
añodenacimiento=eval(input('ingresar año de nacimiento: '))
numerodehijos=eval(input('ingresar numero de hijos: '))
añosdeperteneciaalbanco=eval(input('ingresar años de pertenecia al banco: '))
estadocivil=eval(input('ingresar Estado civil ("1": soltero, "2", casado): '))
dondevive=eval(input('ingresar Si vive en campo o cuidad ("3": urbano, "4": rural): '))

años = añodenacimiento - 2020

if añosdeperteneciaalbanco > 10 and numerodehijos >= 2:
    print('APROBADO')
elif estadocivil == 2 and numerodehijos > 3 and 45 <= años <= 55:
    print('APROBADO')
elif ingresos > 2500000 and estadocivil == 1 and dondevive == 3:
    print('APROBADO')
elif ingresos > 3500000 and añosdeperteneciaalbanco > 5:
    print('APROBADO')
elif dondevive == 4 and estadocivil == 2 and numerodehijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')
