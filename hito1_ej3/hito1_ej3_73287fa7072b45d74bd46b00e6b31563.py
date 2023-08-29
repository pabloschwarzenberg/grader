ingresos = eval(input("ingrese sus ingresos en pesos"))
edad = eval(input("ingrese su año de nacimiento"))
hijos = eval(input("cuantos hijos tiene"))
banco = eval(input("cuanto años lleva en el banco"))
estado = input("estado civil S si es Soltero, o C si es casado")
vive = input("usted vive U urbano o R rural")
edad_actual = (2020 - edad)

#primer caso
if(banco>10 and hijos>=2):
    print("credito aprobado")

   
#segundo caso
elif(estado == "C" and hijos >= 3 and 45<=edad_actual<=55 ):
        print("aprobado")

        #print("no aprobado")
#tercr caso
elif(ingresos>2500000 and vive == "S"and vive=="U"):
            print("aprobado")

           
#cuarto caso
elif(ingresos>350000 and banco>5):
    print("aprobado")

              
#quinto caso
elif(vive=="R"and estado =="C"and hijos<2):
    print("aprobado")
else:
    print("no aprobado")