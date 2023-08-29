seq_uno = input("Ingrese su primera secuencia: ")
seq_dos = input("Ingrese su segunda secuencia: ")

cant1 = len(seq_uno)
cant2 = len(seq_dos)

dif = cant1 - cant2

seq_uno = list(seq_uno)
seq_dos = list(seq_dos)

no_ig = "_"
seq_uno[0:dif] = no_ig
aline = seq_uno
contador = 0
for i in seq_uno:
    if(i != seq_dos[contador]):
        aline[i] = "_"
    else:
        pass
    
    contador+= 1

print(aline)