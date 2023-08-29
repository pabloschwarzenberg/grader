#Aprobación de créditos
#Ingreso (en pesos)
iCLP = int(input("Digite su ingreso en pesos(CLP): "))
#Año de nacimiento
nA = int(input("Año de nacimiento: "))
#Número de hijos
hijos = int(input("Digite numeros de hijos: "))
#Años de pertenencia al banco
pA = int(input("Digite la cantidad de años de pertenencia al banco: "))
#Estado civil ("S": soltero, "C", casado)
eC = input("Digite su estado civil (S: soltero, C, casado): ")
#Si vive en campo o cuidad ("U": urbano, "R": rural)
viv = input("Digite si vive en campo o ciudad (U: urbano, R: rural): ")

aprob = "RECHAZADO"
r = "APROBADO"
edad = 2016-nA

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if(pA > 10 and hijos >= 2) : aprob = r
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
if((eC == "C" or eC == "c") and hijos > 3 and edad > 45 and edad < 55 ) : aprob = r
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
if(iCLP > 2500000 and (eC == "S" or eC == "s") and (viv == "U" or viv == "u")): aprob = r
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
if(iCLP > 3500000 and pA > 5) : aprob = r
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
if((eC == "C" or eC == "c") and (viv == "R" or viv == "r") and hijos < 2) : aprob = r

print(aprob)
