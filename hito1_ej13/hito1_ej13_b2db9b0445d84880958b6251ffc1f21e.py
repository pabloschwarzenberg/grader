x = int(2);
numero = int(input("Ingrese un numero para calcular factor(es) primo(s): "));

while(numero != 1):
        if(numero %x == 0):
            print(str(x)+" ");
            numero=numero/x;
        else:
            x = x+1

