#Contestador de celular
numero_telefonico = input("ingrese numero telefonico ")


if len(numero_telefonico) != 8:
     raise ValueError("debe ser de 8 digitos...")
else:
     numero_telefonico = int(numero_telefonico)
     print("Numero Valido")

hora = int(input("ingrese hora de llamado :" ))
if hora != range(24):
     raise ValueError("hora debe ser de 0 a 23...")
else:
     print("hora valida")

def termina_en_numero(texto):
     patron = '909$'

     return bool(re.serch(patron, texto))

def comienza_en_numero(cadena):
     patron = '^877'

     return bool(re.serch(patron, cadena))

if hora == range(8):
     print("Contestar")
elif hora == range(19, 24):
     print("No Contestar")
        
while hora == range(8, 15):
     if termina_en_numero(numero_telefonico) == True:
        print ("Contestar")
     else:
        print ("No Contestar")
        
while hora == range(17, 20):
     if comienza_en_numero(numero_telefonico) == True:
        print("No Contestar")
     else:
        print("Contestar")
else:
        print("Contestar")     