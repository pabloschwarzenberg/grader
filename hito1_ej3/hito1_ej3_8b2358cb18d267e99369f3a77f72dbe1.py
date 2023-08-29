#Aprobación de créditos


C=0
S=0
U=0
R=0
ingresos = int(input("Por favor, ingrese sus ingresos: "))
añonacimiento = int(input("Por favor, ingrese su fecha de nacimiento: "))
hijos = int(input("Por favor, introduzca la cantidad de hijos: "))
añosdepertenencia = int(input("Por favor, introduzca su cantidad de años con el banco: "))
estadocivil= input("coloque una letra S si es soltero, o C si es casado: ")
campociudad = input("Coloque U si vive es zona urbana o R si vive en zona rural: ")

if añosdepertenencia>10 and hijos>=2:
    print ("APROBADO")
elif estadocivil==C and hijos>3 and añonacimiento>=1967 or añonacimiento<=1977:
    print ("APROBADO2")
elif ingresos>2500000 and estadocivil==S and campociudad==U:
    print("APROBADO")
elif ingresos>3500000 and añosdepertenencia>5:
    print("APROBAMOS")
elif campociudad==R and estadocivil==C and hijos<2:
    print("APROBAMOS")     