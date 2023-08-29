def ocultar_letras(palabra,cantidad):
    import random
    indices=list(range(len(palabra)))
    palabra=list(palabra)
    cantidad=list(range(cantidad))
    aesconder=[]
    for i in cantidad:
        a=random.choice(indices)
        indices.remove(a)
        aesconder.append(a)
    for x in aesconder:
        palabra[x]="_"

    palabra="".join(palabra)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    palabra_secreta=list(palabra_secreta)
    indices=[]
    idx=0
    for i in palabra_secreta:
        if i==letra:
            indices.append(idx)
            idx+=1
        else:
            idx+=1
    for i in indices:
        palabra[i]=palabra_secreta[i]

    palabra="".join(palabra)

    return palabra

if __name__ == "__main__":
    
    import random
    psecretas=["schwarzenberg","informatica","harrypotter","aragorn","manzana","mango","rubia","magovaldivia","superacion","increible","python","java","cocamendoza","estupido","surface","millonario","supercalifragilisticoespialidoso","desoxiribonucleico","ariel"]
    palabra_secreta=random.choice(psecretas)
    if len(palabra_secreta)>=5:
        cantidad=len(palabra_secreta)//5*2
    else:
        cantidad=1

    palabra=ocultar_letras(palabra_secreta,cantidad)

    print("Adivina la palabra : ",palabra)

    i=0
    while i<7:
        print("Elige opcion:\n(1) Adivinar letra\n(2)Adivinar palabra")
        eleccion=input()
        if eleccion=="1":
            palabra=revisar_letra(palabra_secreta,palabra,input("Por cual letra te la juegas?: "))
            print("La palabra ha quedado asi: ",palabra)
            i+=1
            print("Te quedan %s turnos"%(7-i))
        elif eleccion=="2":
            suposicion=input("Por cual palabra te la juegas?: ")
            if suposicion==palabra_secreta:
                print("Acertaste. Felicidades. Ganaste.")
                break
            else:
                i+=1
                print("Erraste")
                print("Te quedan %s turnos" % (7 - i))
    print("Perdiste")

  
         