#Aprobación de créditos
from datetime import datetime

def banco_e_hijos(banco, hijos):
    return banco > 10 and hijos >= 2

def casado_hijo_anios(estado_civil, hijos, anio_nacimiento):
    now = datetime.now()
    return (estado_civil == 'C') and (hijos > 3) and ( ((anio_nacimiento - now.year ) >= 45) and ( (anio_nacimiento - now.year ) <= 55 ))

def soltero_ciudad(ingresos, estado_civil, donde_vive):
    return (ingresos > 2500000) and (estado_civil == 'S') and (donde_vive == 'U')
    
def superior_banco(ingresos, pertenencia_banco):
    return (ingresos > 3500000) and (pertenencia_banco > 5)

def casado_vive_campo(donde_vive, estado_civil, hijos):
    return (donde_vive == 'R') and (estado_civil == 'C') and (hijos < 2)

ingresos = input("Indique sus ingresos (en pesos): ")

if ingresos.isdigit():

    anio_nacimiento = input("Indique Año de nacimiento: ")

    if (len(anio_nacimiento) == 4):
        
        num_hijos = input("Indique número de hijos: ")
        pertenencia_banco = input("Indique años de pertenecia al banco: ")

        if pertenencia_banco.isdigit():

            estado_civil = input("Indique Estado Civil, donde 'S' es soltero y 'C' es casado): ").upper()

            if(estado_civil == 'S' or estado_civil == 'C'):
            
                donde_vive = input("Indique donde vive, 'U' es urbano y 'R' es rural: ").upper()

                if(donde_vive == 'U' or donde_vive == 'R'):

                    if (
                        banco_e_hijos(int(pertenencia_banco), int(num_hijos)) or
                        casado_hijo_anios(estado_civil, int(num_hijos), int(anio_nacimiento)) or
                        soltero_ciudad(int(ingresos), estado_civil, donde_vive) or
                        superior_banco(int(ingresos), int(pertenencia_banco)) or
                        casado_vive_campo(donde_vive, estado_civil, int(num_hijos))
                    ):
                        print("APROBADO")
                    else:
                        print("RECHAZADO")      
                else:
                    print("Zona donde vive es inválida")
            else:
                print("Estado civil inválido")
        else:
            print("Años de pertenencia al banco inválidos")
    else:
        print("Año de nacimiento no válido")
else:
    print("Ingresos no válidos")