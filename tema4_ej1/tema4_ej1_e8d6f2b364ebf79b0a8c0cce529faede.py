print("Bienvenido a ADIVINA-PALABRA")
minimo = 2
maximo = 6
n1 = 0
n2 = 0 
def verificar(t):
    for i in t:
        if i not in caracteres:
            return False
            break
    else:
        return True
def indice(b, t):
    L1 = []
    for e in range(len(t)):
        if t[e] == b:
            L1.append(e)
        else:
            pass
    return L1
def verificar_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
caracteres =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Jugador1 = input("Ingrese el Nombre del jugador '1': ")
Jugador2 = input("Ingrese el Nombre del jugador '2': ")
n1 = int(input("Ingrese la cantidad de palabras que quieren adivinar, (2), (4), (6) : "))
for j in range(1,n1+100):
    if n1%2!= 0:
     print ("dijito incorrecto")
     n1 = int(input("Ingrese la cantidad de palabras que quieren adivinar, (2), (4), (6) : "))
n2 = int(input("Ingrese la cantidad de intentos para jugar,(minimo 2 y maximo 6) : "))
for j in range(1,n2+100):
    if n2<minimo or n2>maximo:
     print("dijito invalido")
     n2 = int(input("Ingrese la cantidad de intentos para jugar,(minimo 2 y maximo 6) : "))
Proponedor = Jugador1
Adivinador = Jugador2
puntaje = 0
Puntaje_Jugador1 = 0
Puntaje_Jugador2 = 0
l1 = [0, 2, 4]
l2 = [1, 3, 5]
i = 0
while i < (n1*2):
    print("Ahora Juega el Proponedor: ", Proponedor)
    for j in range(3):
        palab = input("Proponedor ingrese la palabra a Adivinar: ")
        if (verificar(palab) == True) and (palab.islower() == True) and (len(palab) <= 20):
            palaba_1 = palab
            break
        else:
            continue
    print('Ahora juega el Adivinador: ', Adivinador)
    a = 0
    c1 = 0
    c2 = 0
    h = 0
    f = len(palaba_1)
    while a < (f+c1):
        v1 = input("Que letra cree que tiene la Palabra: ")
        if v1 in palaba_1:
            c1 += 1
            r = palaba_1.count(v1)
            h += r
            print("Esta letra se encuentra en la posicion: ", indice(v1, palaba_1))
            if len(palaba_1) == h:
                puntaje += ((c1/n2) - 1)*len(palaba_1)
                break
        else:
            c2 += 1
            if c2 == 3:
                print("Muy mal, se Acabaron los intentos")
                print("La palabra que debio haber adivinado es: ", palaba_1)
                break
            print("La letra no esta debe volver a ingresar otra letra, suerte")
        a += 1
    Proponedor, Adivinador = Adivinador, Proponedor
    if verificar_par(i) == True:
        Puntaje_Jugador2 += puntaje
    if verificar_par(i) == False:
        Puntaje_Jugador1 += puntaje
    i += 1
if Puntaje_Jugador1 > Puntaje_Jugador2:
    print("")
    print("El jugador ganador es: ", Jugador1, "con ", Puntaje_Jugador1, "puntos FELICIDADES")
    print("El puntaje del jugador ", Jugador2, " es: ", Puntaje_Jugador2, "SUERTE PARA LA PROXIMA")
else:
    print("")
    print("El jugador ganador es: ", Jugador2, "con ", Puntaje_Jugador2, "puntos FELICIDADES")
    print("El puntaje del jugador ", Jugador1, " es: ", Puntaje_Jugador1, "SUER