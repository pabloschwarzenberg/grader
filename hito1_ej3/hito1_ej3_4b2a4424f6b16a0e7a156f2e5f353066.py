#Aprobación de créditos
print('\nAprobación de créditos\n')
print('Ingrese los datos del postulante.\n')

try:
    ingreso = int(input('Ingresos(en pesos): '))
    yNac = int(input('Año de nacimiento: '))
    hijos = int(input('Número de hijos: '))
    yPer = int(input('Número de años de pertenencia al banco: '))
    eCivil = str(input('Estado civil("S": soltero | "C": casado): '))
    residencia = str(input('Dónde vive("U": urbano | "R": rural): '))

    edadP = (2021-yNac)

    #  hijos>=2 and yPer>=10
    
    #  45<=edadP<=55 and hijos >=3 and eCivil == 'C'
    
    #  ingreso>=2500000 and eCivil== 'S' and residencia == 'U'
    
    #  ingreso>=3500000 and yPer>=5
    
    #  hijos >=2 and eCivil == 'C' and residencia == 'R'
    
    if eCivil == 'S' or 'C' and residencia == 'U' or 'R':

       if hijos>=2:

           if yPer>=10:
               print('APROBADO')

       if edadP>=45 and edadP<55:

           if hijos>=3:

               if eCivil =='C':
                   print('APROBADO')            

       if ingreso>=2500000:
           
            if eCivil == 'S':

                if residencia == 'U':
                    print('APROBADO')
           

       if ingreso>=3500000:

            if yPer>=5:
                print('APROBADO')


       if hijos<2:
           
           if eCivil == 'C':
               
               if residencia == 'R':
                   print('APROBADO')

       
                 

    else:
      print('Porfavor use los carácteres especificados')



except:
 print('Entradas Inválidas')
     