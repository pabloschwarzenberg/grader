# completa el código de la función
nu = int(2);
x = int(input("+Favor de ingresar el número:"))

while (x != 1):

    if (x % nu == 0):
        print(str(nu) + " ");
        x = x / nu;

    else:
        nu = nu + 1;  