def jerigonzo(string):
    a=list(string)

    for i in range(len(a)):
        if(a[i]=='a'):
            a[i]="apa"

        elif (a[i]== 'e'):
            a[i]="epe"
        elif (a[i] == 'i'):
            a[i]="ipi"
        elif (a[i] == 'o'):
            a[i]="opo"
        elif (a[i] == 'u'):
            a[i]="upu"
    cadena = "".join(a)

    return cadena
if __name__ == "__main__":
    palabra=input("ingrese palabra:")
    j=jerigonzo(palabra)
    print(j)