#Aprobación de créditos
Income = int(input("¿Cuál es su ingreso en CLP? "))
Age = 2022 - int(input("Año de nacimiento: "))
Childs = int(input("Cantidad de Hijos: "))
Years = int(input("Años de pertenencia al banco: "))
CivilStatus = input("Estado Civil ('S': soltero ; 'C': casado): ")
Home = input("Vives en campo o ciudad? ('U': Urbano ; 'R': rural): ")


#Adaptación de Variables

Married = False
City = False

if (CivilStatus == 'C'):
	Married=True

if (Home == 'U'):
	City=True

#Debug

print(Income)
print(Age)
print(Childs)
print(Years)
print(Married)
print(City)

#Proceso de Decisión

y = 'APROBADO'
n = 'RECHAZADO'

if((Years > 10) and (Childs >= 2)):
	print(y)

elif((Married) and (Childs > 3) and (45 <= Age <= 55)):
	print(y)

elif((Income > 2500000) and (not Married) and (City)):
	print(y)

elif((Income > 3500000) and (Years > 5)):		
	print(y)

elif(not(City) and (Married) and (Childs < 2)):
	print(y)

else:
	print(n)