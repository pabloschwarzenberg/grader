from random import *

def ocultar_letras(palabra,cantidad):
    pal_ = len(palabra)*"_"
    pal_ = list(pal_)
    lista_n = []
    for i in range(len(palabra)):
        lista_n += str(i)
    indice = sample(lista_n,cantidad) 
    for i in range(cantidad):
        numero = int(indice[i])
        pal_[numero] = palabra[numero]
    pal_ = "".join(pal_)
    return pal_ 

def revisar_letra(palabra_secreta,palabra,letra,pista_inicial):
    if(len(palabra)>1):
        if(palabra == palabra_secreta):
            return palabra_secreta
        else:
            return palabra
    elif(len(letra)==1):
        if(letra in palabra_secreta):
            busc = palabra_secreta.find(letra)
            pista_inicial = list(pista_inicial)
            pista_inicial[busc] = letra
            pista_final = "".join(pista_inicial)
            return pista_final
        else:
            return pista_inicial

if __name__ == "__main__":
    palabras = "lepidoptero dinosaurio".split()
    p_Sec = choice(palabras) 
    pista = ocultar_letras(p_Sec,4) 
    print(p_Sec,pista)
    contador = 0 
    while(contador<7):
        Int_User = input("Ingrese intento {} : ".format(contador+1)).lower()
        pista2 = revisar_letra(p_Sec,Int_User,Int_User,pista)
        pista = pista2
        if((Int_User == p_Sec)or(pista2 == p_Sec)):
            print("Ganaste")
            break
        elif(len(Int_User)== 1)and(Int_User!=p_Sec):
            print(pista2)
        else:
            print("Casi!!!....Intentalo otra vez")
        contador+=1