#DESCOMPONER FACTORES
x = int(2);
numeross = int(input("Ingrese numero : "));
while (numeross != 1):


    if (numeross % x == 0):

        print(str(x)+ " ");
        numeross = numeross /x;

    else:

        x = x + 1
           