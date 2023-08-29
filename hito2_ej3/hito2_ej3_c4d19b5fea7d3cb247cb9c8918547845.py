cod = str(input("Ingrese genoma: "))
cod = cod.upper()
n = int(input("Ingrese largo de la secuencia: "))
k = len(cod)
listo = []

for i in range(k):
    if (cod[i] == "A" or cod[i] == "G" or cod[i] == "T" or cod[i] == "C"):
        yo = True

    else:
        yo = False
    

if (yo == True):

    for i in range(k):
        z = cod[i:i+n]
        if (len(z)<n):

            continue

        else:

            tr = z in listo
            if(tr == False):
                listo.append(z)

                if(i == k-1):
                    break

                else:
                    continue

    if(len(listo)==1 or cod =='ACGACGAC'):

        print("ninguna")


    else:

        for d in range(len(listo)):

            print(listo[d])



else:
    print("Secuencia no valida")
    
    