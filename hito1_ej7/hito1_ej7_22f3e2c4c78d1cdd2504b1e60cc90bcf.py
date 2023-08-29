#Zodiaco
zodiaco=["Aries","Tauro","Gemini","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]


dia=int(input("Ingrese un Día del mes:"))
if dia<=31:
    mes=int(input("Ingrese un mes del 1 al 12: "))
    if mes<=12:
        if mes==3 and dia>=21 or mes==4 and dia<20:
            print(f"Su signo del sodiaco es {zodiaco[0]}")
        elif mes==4 and dia>=20 or mes==5 and dia<21:
            print(f"Su signo del sodiaco es {zodiaco[1]}")
        elif mes==5 and dia>=21 or mes==6 and dia<21:
            print(f"Su signo del sodiaco es {zodiaco[2]}")
        elif mes==6 and dia>=21 or mes==7 and dia<23:
            print(f"Su signo del sodiaco es {zodiaco[3]}")
        elif mes==7 and dia>=23 or mes==8 and dia<23:
            print(f"Su signo del sodiaco es {zodiaco[4]}")
        elif mes==8 and dia>=23 or mes==9 and dia<23:
            print(f"Su signo del sodiaco es {zodiaco[5]}")
        elif mes==9 and dia>=23 or mes==10 and dia<23:
            print(f"Su signo del sodiaco es {zodiaco[6]}")
        elif mes==10 and dia>=23 or mes==11 and dia<22:
            print(f"Su signo del sodiaco es {zodiaco[7]}")
        elif mes==11 and dia>=23 or mes==12 and dia<22:
            print(f"Su signo del sodiaco es {zodiaco[8]}")
        elif mes==12 and dia>=22 or mes==1 and dia<20:
            print(f"Su signo del sodiaco es {zodiaco[9]}")
        elif mes==1 and dia>=20 or mes==2 and dia<19:
            print(f"Su signo del sodiaco es {zodiaco[10]}")
        elif mes==2 and dia>=19 or mes==3 and dia<21:
            print(f"Su signo del sodiaco es {zodiaco[11]}")
        else:
            print(f"Fecha Invalida")
            
    else:
        print(f"Ingrese mes valido.")
else:
    print("Ingrese día valido.")