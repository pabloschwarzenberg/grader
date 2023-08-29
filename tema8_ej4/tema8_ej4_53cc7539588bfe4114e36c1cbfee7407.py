palabra_l=[]
listo=""
def rot13(palabra):
    palabra_l = list(palabra)
    for n in range(0,len(palabra_l)):
        if palabra_l[n] == "a" or palabra_l[n] == "A":
            palabra_l[n]="n"
        elif palabra_l[n] == "b" or palabra_l[n] == "B":
            palabra_l[n]="o"
        elif palabra_l[n] == "c" or palabra_l[n] == "C":
            palabra_l[n]="p"
        elif palabra_l[n] == "d" or palabra_l[n] == "D":
            palabra_l[n]="q"
        elif palabra_l[n] == "e" or palabra_l[n] == "E":
            palabra_l[n]="r"
        elif palabra_l[n] == "f" or palabra_l[n] == "F":
            palabra_l[n]="s"
        elif palabra_l[n] == "g" or palabra_l[n] == "G":
            palabra_l[n]="t"
        elif palabra_l[n] == "h" or palabra_l[n] == "H":
            palabra_l[n]="u"
        elif palabra_l[n] == "i" or palabra_l[n] == "I":
            palabra_l[n]="v"
        elif palabra_l[n] == "j" or palabra_l[n] == "J":
            palabra_l[n]="w"
        elif palabra_l[n] == "k" or palabra_l[n] == "K":
            palabra_l[n]="x"
        elif palabra_l[n] == "l" or palabra_l[n] == "L":
            palabra_l[n]="y"
        elif palabra_l[n] == "m" or palabra_l[n] == "M":
            palabra_l[n]="z"
        elif palabra_l[n] == "n" or palabra_l[n] == "N":
            palabra_l[n]="a"
        elif palabra_l[n] == "o" or palabra_l[n] == "O":
            palabra_l[n]="b"
        elif palabra_l[n] == "p" or palabra_l[n] == "P":
            palabra_l[n]="c"
        elif palabra_l[n] == "q" or palabra_l[n] == "Q":
            palabra_l[n]="d"
        elif palabra_l[n] == "r" or palabra_l[n] == "R":
            palabra_l[n]="e"
        elif palabra_l[n] == "s" or palabra_l[n] == "S":
            palabra_l[n]="f"
        elif palabra_l[n] == "t" or palabra_l[n] == "T":
            palabra_l[n]="g"
        elif palabra_l[n] == "u" or palabra_l[n] == "U":
            palabra_l[n]="h"
        elif palabra_l[n] == "v" or palabra_l[n] == "V":
            palabra_l[n]="i"
        elif palabra_l[n] == "w" or palabra_l[n] == "W":
            palabra_l[n]="j"
        elif palabra_l[n] == "x" or palabra_l[n] == "X":
            palabra_l[n]="k"
        elif palabra_l[n] == "y" or palabra_l[n] == "Y":
            palabra_l[n]="l"
        elif palabra_l[n] == "z" or palabra_l[n] == "Z":
            palabra_l[n]="m"
    listo="".join(palabra_l)
    return listo

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           