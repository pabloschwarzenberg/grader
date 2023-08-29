import sys
s_c = 10000000
s_i = 100000 
us = 10334151
clv = 1803
u = 0
n_n=0
n_s=0
while n_s != "S":
    while u!= us:
        u=int(input("Ingrese su usuario: "))
        if u != us:
            print("Usuario invalido")
            sys.exit()
        cl_u=0
        count=0
        while cl_u!= clv:
            cl_u= int(input("Ingrese su clave: "))
            count += 1
            if cl_u != clv and count!=0:
                print("Clave invalida le quedan",3-count,"intentos")
            elif count==0:
                sys.exit("Tarjeta Bloqueada")
    print("log in successfully")
    if __name__ == "__main__":
        mont=int(input("Ingrese un monto a retirar: "))
        if mont<s_c:
            s_c -= mont
            s_i -= mont
            print("Saldo disponible en el cajero corresponde a $",s_c)
            print("Saldo disponible en su cuenta corresponde a $",s_i)
        else:
            print("Monto invalido")
        n_s=input("Desea dejar de ejecutar S/N: ")
        n_s.upper()
print("Cuenta cerrada con exito")