#Aprobación de créditos
from datetime import date

today = date.today()

yearNow = today.strftime("%Y")
#print("yearNow =", yearNow)

valuePesos=int(input("Ingreso (en pesos): "))
valueBirth=int(input("Año de nacimiento: "))
valueSons=int(input("Número de hijos: "))
valueYearsOfBank=int(input("Años de pertenencia al banco: "))
valueMaritaStatus=input("Estado civil - 'S' soltero, 'C' casado: ")
valueCountrysideCity=input("Si vive en campo o cuidad - 'U' urbano, 'R' rural: ")

valueMaritaStatus = valueMaritaStatus.upper()
valueCountrysideCity = valueCountrysideCity.upper()

difDate = int(yearNow) - valueBirth
#print("Idad: ", difDate)

if valueYearsOfBank >= 10 and valueSons >= 2  :
    print("APROBADO")
elif valueMaritaStatus == "C" and valueSons > 3 and difDate >= 45 and difDate <= 55 :
    print("APROBADO")
elif valuePesos >= 2500000 and valueMaritaStatus == "S" and valueCountrysideCity == "U" :
    print("APROBADO")
elif valuePesos >= 3500000 and valueYearsOfBank > 5 :
    print("APROBADO")
elif  valueCountrysideCity == "R" and valueMaritaStatus == "C" and valueSons < 2 :
    print("APROBADO")
else :
    print("RECHAZADO")      