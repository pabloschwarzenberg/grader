ingreso = float(input('Ingresos en millones: '))
ingreso_formateado = format(ingreso * 1000000, ",.0f")  # Formatear el ingreso con separador de miles y ceros

ano = int(input('Ponga su año de nacimiento: '))
hijos = int(input('Ingrese la cantidad de hijos: '))
anos_de_pertenencia_al_banco = int(input('Ingrese cuántos años lleva con el banco: '))
estado_civil = input('Ingrese su estado civil "s": soltero, "c": casado: ')
vive = input('Ingrese si vive en campo o ciudad ("u": urbano, "r": rural): ')

if ingreso >= 2.5:
    print('DENEGADO')
elif any(valor <= 0 for valor in [ingreso, ano, hijos, anos_de_pertenencia_al_banco]):
    print('Datos ingresados inválidos.')
elif anos_de_pertenencia_al_banco >= 10 and hijos >= 2:
    print('APROBADO')
elif estado_civil == 'c' and hijos >= 3 and 45 <= (2023 - ano) <= 55:
    print('APROBADO')
elif ingreso >= 3.5 and anos_de_pertenencia_al_banco >= 5:
    print('APROBADO')
elif vive == 'r' and estado_civil == 'c' and hijos < 2:
    print('APROBADO')
else:
    print('DENEGADO')

print("Ingresos formateados:", ingreso_formateado)
