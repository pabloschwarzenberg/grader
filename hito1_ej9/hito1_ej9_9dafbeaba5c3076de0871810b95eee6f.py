#SISTEMA DE ESCUACIONES
numeros = input("Ingrese los 6 números reales de las 2 ecuaciones: ")
#Separar las ecuaciones
#Ecuación 1
primerX = numeros[:1]
primerX = int(str(primerX))
primerY = numeros[2:3]
primerY = int(str(primerY))
primerNum = numeros[4:5]
primerNum = int(str(primerNum))


#Ecuación 2
segundoX = numeros[6:7]
segundoX = int(str(segundoX))
segundoY = numeros[8:9]
segundoY = int(str(segundoY))
segundoNum = numeros[10:11]
segundoNum = int(str(segundoNum))

#Crear las ecuaciones (1 y 2) para resolver el sistema de ecuaciones
#Ecuación 1
ecuacion1 = str(primerX) + "x"  "+" + str(primerY) + "y" + "=" + str(primerNum)

#Ecuación 2
ecuacion2 = str(segundoX) + "x"  "+" + str(segundoY) + "y" + "=" + str(segundoNum)
#Resolver sistema
#Primera parte despejar Y
PrimeraPartex1 = (segundoX*primerNum)
PrimeraPartex2 = (primerX*segundoNum)

#Segunda parte despejar Y
SegundaPartex1 = segundoX*(primerY)
SegundaPartex2 = primerX*(segundoY)

#Tercera parte despejar Y
TerceraPartex1 = PrimeraPartex1 - PrimeraPartex2
TerceraPartex2 = SegundaPartex1 - SegundaPartex2

#Despejar Y
y = TerceraPartex1/TerceraPartex2
resultadoY = "y" + "=" + str(y)


#Reemplazar Y y resolver X
x = (primerNum -(primerY * y ))/primerX
resultadoX = "x" + "=" + str(x)

print(resultadoX)
print(resultadoY)




      