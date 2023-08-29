#Cajero Automático
import os
print("bienvenido cajero automatico")
c = 5467
x = int(input("ingrese su contraseña:" ))
def contraseña():
 
    if (x == c):
 
        print("contraseña correcta")
    else:
        print("contraseña incorrecta")
 
 
contraseña()

os.system("cls")
def menu():
    print("menu")
    print("1. Depositar")
    print("2. retirar")
    print("3. ver saldo")
 

menu()
 
monto=1000000
 
def depositar():
 
    dep = int(input("ingrese su monto a depositar:"))
    print("usted a depositado",dep)
 
 
depositar()
 
 
 
os.system("cls")
 
 
menu()
 
 
def giro():
    girar=int(input("cuanto desea girar: "))
    print("su monto actual es", monto - girar)
    print("usted a retirado" , girar)
 
giro()
 
os.system("cls")
 
menu()
 
def ver():
    print("su saldo es" , monto)
ver()
 
 
 
 
 
 
"""cajero automatico"""
import os
name="claudio"
print("bienvenido")
 
contra = "5467"
 
pasword=int(input("ingrese su contraseña:"))
 
 
 
if pasword == contra:
    print("contraseña correcta","bienvenido",name)
 
 
else:
    print("contraseña incorrecta")
 
 
 
 
"""menu"""
os.system("cls")
print("menu")
print:("opcion1. depositar")
print:("opcion2. retirar")
print:("opcion2. ver saldo")
opcion= int (input("escoja opcion: "))
 
 
os.system("cls")
 

if opcion == 1:
    depositar=int(input("cuanto desea depositar:"))
 
    print("usted a depositado",depositar)
 

saldo = 1000000
 
if opcion==2:
    giro=int(input("cuanto desea retirar:"))
    print("su saldo actual es" , saldo - giro)
    print("usted a retirado" , giro)
 

if opcion==3:
    print("su saldo es", saldo)