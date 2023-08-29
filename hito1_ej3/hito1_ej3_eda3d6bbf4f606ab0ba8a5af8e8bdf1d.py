import os
edad=0
op=0
ingr_p=0
a_nacim=0
num_hijos=0
a_en_banco=0
est_cvl="soltero"
ciud_cam="U"
rep=1
while rep==1:
    os.system("cls")
    print('''
    Aprobación de creditos:
    ''')
    
    os.system("pause")
    os.system("cls")
    while  ingr_p<=20000:
        os.system("cls")
        ingr_p=int(input("Ingrese su ingreso en pesos: $"))
        if ingr_p>=20000:
            print("Datos aprobados")
        else:
            print("Datos rechazados")

        os.system("pause")
                    
    
    while a_nacim<1995 or a_nacim>2002:
        os.system("cls")
         a_nacim=int(input("Ingrese año de su nacimiento: "))
        edad=2020-a_nacim
        if a_nacim > 1995 and a_nacim<2002:
            print("Datos aprobados")
        else:
            print("Reprobado")
        
        os.system("pause")
    while num_hijos>15 or num_hijos<0:
        os.system("cls")
        num_hijos=int(input("Ingrese la cantidad de hijos que tiene: "))
        if num_hijos>= 0 and num_hijos<6:
            print("Datos aprobados")
        elif num_hijos>=6:
            print("Datos Aprobados pero, ¿usted es udi su pareja es su prima?")
        else:
            print("Datos rechazados")
        
        os.system("pause")
    while a_en_banco<0 or a_en_banco>47:
        os.system("cls")
        a_en_banco=int(input("Ingrese años que usted lleva en el banco: "))
        op=edad-a_en_banco
        if op<=0:
            print("Datos aprobados")
        else:
            print("Datos rechazados")
        
        os.system("pause")
    while est_cvl!="S" and est_cvl!="C" :
        os.system("cls")
        est_cvl=str(input("Ingrese en mayusculas 'S' o 'C' para indicar su estado civil: "))
        if est_cvl=="S" or est_cvl=="C":
            print("Datos aprobados")
        else:
            print("Datos rechazados")
        
        os.system("pause")
    while est_cvl!="R" and est_cvl!="U" :
        os.system("cls")
        ciud_cam=str(input('''¿Usted vive en?:
        Ingrese 'U' para ciudad o 'R' para campo: '''))
        if est_cvl=="S" or est_cvl=="U":
            print("Datos aprobados")
        else:
            print("Datos rechazados")
        
        os.system("pause")
    
    os.system("cls")
    print("Para saber la resolucion de su consulta:")
    os.system("pause")
    os.system("cls")
    print("____RESULTADO____:")
    if op>10 and num_hijos>=2:
        print("Credito aprobado")
    elif est_cvl=="S" and num_hijos>3 and 55>edad>45:
        print("Credito aprobrado")
    elif ingr_p>2500000 and est_cvl=="S" and ciud_cam=="U":
        print("Credito aprobado")
    elif ingr_p>3500000 and op>5:
        print("Credito aprobado")
    elif ciud_cam=="R" and num_hijos<2:
        print("Credito aprobado")
    else:
        print("Credito Reprobado")
    os.system("pause")
    rep=int(input("Ingrese 1 para continuar 0 para cerrar: "))