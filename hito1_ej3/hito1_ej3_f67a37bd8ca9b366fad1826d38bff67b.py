#Aprobación de créditosIng=int(input("Ingresos(Pesos):"))
Ing=int(input("Ingresos(Pesos):"))                        
Nac=int(input("Año de nacimiento: "))                     
NH=int(input("Número de hijos: "))                        
Pert=int(input("Años de pertenencia al banco: "))         
est=str(input("Estado civil (S: soltero, C: casado): "))  
Viv=str(input("Vivienda (U: Urbano, R: Rural): "))        
Edad=2021-Nac                                             
if Pert>=10 and NH>=2:                                    
    print("APROBADO")                                     
else:                                                     
    if est== "C" and NH > 3 and 55 > Edad > 45:           
        print("Aprobado")                                 
    else:                                                 
        if est=="S":                                      
            if Viv=="U" and Ing>2500000:                  
                print("APROBADO")                         
        else:                                             
            if Ing>3500000 and Pert>5:                    
                print("APROBADO")                         
            else:                                         
                if est=="C":                              
                    if Viv=="R" and NH<2:                 
                        print("APROBADO")                 
                else:                                     
                    print("RECHAZADO")                    
                                                          