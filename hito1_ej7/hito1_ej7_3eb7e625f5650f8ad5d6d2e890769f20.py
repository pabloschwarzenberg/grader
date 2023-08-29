#Zodiaco
def obtener_signo(dia, mes):
 if mes == 1:
   if dia <= 20:
     return "Capricornio"
   else:
     return "Acuario"
 elif mes == 2:
   if dia <= 18:
     return "Acuario"
   else:
     return "Piscis"
 elif mes == 3:
   if dia <= 20:
     return "Piscis"
   else:
     return "Aries"
 elif mes == 4:
    if dia <= 19:
     return"Aries"
    else: 
     return "Tauro"
 elif mes == 5:
    if dia <= 20:
     return "Tauro"
    else:
     return "Geminis"
 elif mes == 6:
    if dia <= 20:
     return "Geminis"
    else: 
     return "Cancer"
 elif mes == 7:
    if dia <= 22:
     return "Cancer"
    else: 
     return "Leo"
 elif mes == 8:
   if dia <= 22:
     return "Leo"
   else: 
     return "Virgo"
 elif mes == 9:
   if dia <= 22:
     return "Virgo"
   else:
     return "Libra"
 elif mes == 10:
   if dia <= 22:
     return "Libra"
   else:
     return "Escorpio"
 elif mes == 11: 
   if dia <= 21:
     return "Escorpio"
   else:
     return "Sagitario"
 elif mes == 12:
   if dia <= 21:
     return "Sagitario"
   else: 
     return "Capricornio"
 else:
   return "Fecha invalida"

dia = int(input("ingrese su dia de nacimiento: [1-31]"))  
mes = int(input("ingrese su mes de nacimiento: [1-12]"))
signo = obtener_signo(dia, mes)
print("Su signo zodiacal es: ", signo)