def main():
    ingreso = int(input("Ingresa tu ingreso en pesos: "))
    nacimiento = int(input("Ingresa tu año de nacimiento: "))
    hijos = int(input("Ingresa tu número de hijos: "))
    antiguedad = int(input("Ingresa tus años de pertenencia al banco: "))
    estado_civil = input("Ingresa tu estado civil (S para soltero, C para casado): ")
    residencia = input("¿Vives en campo o ciudad? (U para urbano, R para rural): ")
    edad = 2023 - nacimiento
    if antiguedad > 10 and hijos >= 2:
        print("APROBADO")
    elif estado_civil == "C" and hijos > 3 and 45 <= edad <= 55:
        print("APROBADO")
    elif ingreso > 2500000 and estado_civil == "S" and residencia == "U":
        print("APROBADO")
    elif ingreso > 3500000 and antiguedad > 5:
        print("APROBADO")
    elif residencia == "R" and estado_civil == "C" and hijos < 2:
        print("APROBADO")
    else:
        print("RECHAZADO")
if __name__ == "__main__":
    main()