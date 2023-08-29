ingresos=int(input("Ingrese sus ingresos en pesos"))
adn=int(input("Ingrese su año de nacimiento"))
edad=2020-adn
ndh=int(input("Ingrese su numero de hijos"))
añdp=int(input("Ingrese sus años de pertenecencia al banco"))
ec=input("Ingrese su estado civil, S: soltero y C: casado")
coc=input("Ingrese si vive en campo o ciudad, U: urbano y R: rural")
if(ndh>2 or añdp>10):
    print("APROBADO")
elif(ec=="C" or ndh>3 or edad>45 or edad<55 ):
    print("APROBADO")
elif(ingresos>2500000 or ec=="S" or coc=="U"):
    print("APROBADO")
elif(ingresos<3500000 or añdp>5):
    print("APROBADO")
elif(coc=="R" or ec=="C" or ndh>2):
    print("APROBADO")
else:
        print("RECHAZADO")