usuario_r= "10334151"
clave_r= "1803"
Saldo_c=1000000
Saldo_u=100000
b20=20
b10=40
b5=40
def Validar(usuario,clave):
    if usuario!=usuario_r or clave!=clave_r:
        print("clave invalida")
        return False
    else:
        return True
def Validar_monto(retiro):
    if retiro>Saldo_c or retiro>Saldo_u:
        return False
    else:
        return True
usuario=""
if usuario!="N":
    intentos=3
    while intentos>0:
        usuario=input()
        clave=input()
        if Validar(usuario,clave)==False:
            intentos-=1
            
        else:
            retirar=int(input())
            if Validar_monto(retirar)==False:
                print("monto no permitido")
            else:
                Saldo_c-=retirar
                Saldo_u-=retirar
                print("saldo cuenta=",Saldo_u, "saldo cajero=",Saldo_c)  
                if retirar%10000==0:
                  a=retirar//20000
                  b=retirar%20000
                  print("billetes 20000={0}".format(a))
                  print("billetes 10000={0}".format(b))
                  print("billetes 5000=0")
                else:
                  a=retirar//20000
                  b=(retirar%20000)//10000
                  c=((retirar%20000)%10000)//5000
                  print("billetes 20000={0}".format(a))
                  print("billetes 10000={0}".format(b))
                  print("billetes 5000={0}".format(c))
            break
    if intentos==0:
       print("tarjeta bloqueda")
        
else:
    False