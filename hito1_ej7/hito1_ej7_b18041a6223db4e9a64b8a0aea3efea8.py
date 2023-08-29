#Zodiaco
dia = eval(input("Ingrese su día de nacimiento: "))
mes = eval(input("Ingrese su mes de nacimiento: "))



if mes == 1 and 31 >= dia > 20  or mes == 2 and 19 > dia >= 1:
    print("Acuario.")
elif mes == 2 and  19 > dia >= 31 or mes == 3 and 21 > dia >= 1:
    print("Piscis.")
elif mes == 3 and  31 >= dia >= 21 or mes == 4 and 20 > dia >= 1:
    print("Aries")
elif mes == 4 and  31 >= dia > 20 or mes == 5 and 21 > dia >= 1:
    print ("Tauro")
elif mes == 5 and 31 >= dia > 21 or mes == 6 and  21 > dia >= 1:
     print ("Geminis")
elif mes == 6 and 31 >= dia > 21 or mes == 7 and  23 > dia >= 1:
     print ("Cancer")
elif mes == 7 and 31 >= dia > 23 or mes == 8 and 23 > dia >= 1:
     print ("Leo")
elif mes == 8 and 31 >= dia > 23 or mes == 9 and 23 > dia >= 1:
    print("Virgo")
elif mes == 9 and 31 >= dia > 23 or mes == 10 and 23 > dia >= 1:
    print("Libra")
elif mes == 10 and 31 >= dia > 23  or mes == 11 and 22 > dia >= 1:
    print("Escorpio")
elif mes == 11 and  31 >= dia > 22 or mes == 12 and 22 > dia >= 1:
    print("Sagitario")
if mes == 12 and 31 >= dia > 22 or mes == 1 and 20 > dia >= 1:
    print ("Capricornio")