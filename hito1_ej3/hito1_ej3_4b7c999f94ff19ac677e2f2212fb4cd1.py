#Aprobación de créditos
i =int(input("Ingrese sus ingresos en pesos "))
a =int(input("Ingrese su año de nacimiento "))
n =int(input("Ingrese la cantidad de hijos "))
ab =int(input("Ingrese la cantidad de años que lleva en el banco "))
e =input("Ingrese su estado civil, una C  si esta casado o una S si esta soltero ")
l =input("Ingrese su lugar de residencia, U de urbano o R de rural ")

if ab>10 and n>=2:
    print("APROBADO")
elif e=='C' and n>3 and 1977>=a and a<=1967:
    print("APROBADO")
elif i>2500000 and e=='S' and l=='U':
    print("APROBADO")
elif i>3500000 and ab>5:
    print("APROBADO")
elif l=='R' and e=='C' and n<2:
    print("APROBADO")
else:
    print("RECHAZADO")     