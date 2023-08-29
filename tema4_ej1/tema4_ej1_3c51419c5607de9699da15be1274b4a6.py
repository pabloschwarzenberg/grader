import random
def string_lista(strs):
    lista = []
    for i in strs:
        lista.append(i)
    return lista
def lista_string(lista):
    strs = "".join(lista)
    return strs
def buscar_todas(strs,s):
    strs.lower()
    s.lower()
    todas = []
    num = []
    n = 0
    while n < len(strs):
       a = strs.find(s,n)
       if a == -1:
           break
       if a != -1:
           todas.append(a)
       n += 1
    i = 0
    while i < len(todas):
        b = todas[i]
        a = todas.count(b)
        if a == 1:
            num.append(b)
            i += 1
        else:
            todas.remove(b)
            num.append(b)
            i += a
    return num
def ocultar_letras(txt,num):
    e = 0
    letras = []
    while e < len(txt):
        a = txt[e]
        letras.append(a)
        e += 1
    while num != 0:
        b = random.choice(letras)
        c = letras.index(b)
        letras.remove(b)
        letras.insert(c,"_")
        num -= 1
    oculta = lista_string(letras)
    return oculta
def revisar_letra(txt,txt1,txt2,let): # txt=palabra secreta #txt1=palabra ingresada txt2=palabra oculta
    z = 0
    if txt1 != "0":
        if txt == txt1:
            z = "Felicitaciones, ha adivinado"
        elif txt != txt1:
            z = "La palabra no es la correcta"
    if let != "0":
        pos = buscar_todas(txt,let)
        if pos == []:
            z = "La letra no se encuentra en la palabra"
        else:
            strs1 = string_lista(txt2)
            i = 0
            while i < len(pos):
                strs1[(pos[i])] = let
                i += 1
            strs1 = lista_string(strs1)
            z = "Muy bien, la palabra es %s" % strs1
            global palabraoculta
            palabraoculta = strs1
    return z
if __name__=="__main__":
    palabrasecreta = ["hipercaracterizacion","nacionalsindicalismo","inconstitucionalidad","poligoencefalomeningomielitis","esternocleidomastoideo","otorrinolaringologia","electroencefalograma","ciclopentanoperhidrofenantreno","desoxirribonucleotido"]
    secreta = random.choice(palabrasecreta)
    ocultar = 0
    if len(secreta) < 20:
        ocultar = 11
    if 20 <= len(secreta) < 25:
        ocultar = 17
    if len(secreta) <= 25:
        ocultar = 24
    palabraoculta = ocultar_letras(secreta,ocultar)
    print("La palabra a adivinar es:",palabraoculta)
    print("Tiene siete intentos para adivinar la palabra")
    cont = 0
    while cont < 8:
        opcion = int(input("¿Desea ingresar una (1)palabra o una (2)letra?:"))
        letra = "0"
        palabra = "0"
        if opcion == 1:
            palabra = str(input("Ingrese la palabra: "))
            palabra = palabra.lower()
        if opcion == 2:
            letra = str(input("Ingrese una letra que pueda estar contenida en la palabra: "))
            letra = letra.lower()
        h = revisar_letra(secreta,palabra,palabraoculta,letra)
        print(h)
        if h == "Felicitaciones, ha adivinado":
            break
        if not("-" in h) and not("letra" in h):
            print("Felicitaciones, ha adivinado")
            break
        cont += 1
    if cont >= 8:
        print("Ha perdido")
