import random
i=5
numero=random.randint(0, 20)
print ("hola amig@,adivina cual es el numero que estoy pensando,el numero esta entre 0 y 20.")

while (i)<5:
    print ("ingresa el numero que crees que es:")
    n_usuario= int(input())

    if n_usuario == numero:
        print("usted a adivinado")
        break

    elif (n_usuario) <(numero):
        i=+1
        print ("el numero muy bajo")
    elif (n_usuario) > (numero):
        i=+1
        print ("el numero es muy alto")
    else:
        break

print("El programa ha terminado")
      