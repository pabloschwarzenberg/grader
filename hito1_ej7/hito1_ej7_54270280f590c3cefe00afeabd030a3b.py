dia = int(input("Ingrese día: "))
mes = input("Ingrese mes: ")
if mes == "1" and dia >= 20 or mes == "2" and dia <= 19:
    print("acuario.")
elif mes == "2" and dia >= 19 or mes == "3" and dia <= 21:
    print("piscis.")    
elif mes == "3" and dia >= 21 or mes == "4" and dia <= 20:
    print("aries.")
elif mes == "4" and dia >= 20 or mes == "5" and dia <= 21:
    print("Tauro.")
elif mes == "5" and dia >= 21 or mes == "6" and dia <= 21:
    print("geminis.")
elif mes == "6" and dia >= 21 or mes == "7" and dia <= 23:
    print("cancer.")
elif mes == "7" and dia >= 23 or mes == "8" and dia <= 23:
    print("leo.")
elif mes == "8" and dia >= 23 or mes == "9" and dia <= 23:
    print("virgo.")
elif mes == "9" and dia >= 23 or mes == "10" and dia <= 23:
    print("libra.")
elif mes == "10" and dia >= 23 or mes == "11" and dia <= 22:
    print("escorpio")
elif mes == "11" and dia >= 22 or mes == "12" and dia <= 22:
    print("sagitario.")
else:
    mes == "12" and dia >= 22 or mes == "1" and dia <= 20
    print("capriconio.")
         