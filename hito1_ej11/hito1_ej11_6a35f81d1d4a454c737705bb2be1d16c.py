#Cajero Automático
# Definir las variables iniciales
saldo_cajero = 1000000 # saldo del cajero
saldo_cuenta = 100000 # saldo de la cuenta del usuario
intentos = 0 # contador de intentos fallidos

# Definir un diccionario para guardar los usuarios y claves
usuarios = {10334151: 1803, 12345678: 4321, 87654321: 1234}

# Definir las variables para los billetes
billetes_20000 = 20 # cantidad de billetes de 20000
billetes_10000 = 40 # cantidad de billetes de 10000
billetes_5000 = 40 # cantidad de billetes de 5000

# Definir una función para validar la clave
def validar_clave(clave):
    global intentos # usar la variable global de intentos
    clave_ingresada = int(input("Ingrese su clave: ")) # pedir la clave al usuario
    if clave_ingresada == clave: # si la clave es correcta
        return True # devolver True
    else: # si la clave es incorrecta
        intentos += 1 # aumentar el contador de intentos en uno
        if intentos < 3: # si aún quedan intentos
            print("Clave inválida") # imprimir el mensaje de error
            return validar_clave(clave) # volver a llamar a la función recursivamente con la misma clave
        else: # si no quedan intentos
            print("Tarjeta bloqueada") # imprimir el mensaje de bloqueo
            return False # devolver False

# Definir una función para distribuir el monto entre los billetes
def distribuir_monto(monto):
    global billetes_20000, billetes_10000, billetes_5000 # usar las variables globales de billetes
    b_20000 = 0 # contador de billetes de 20000 entregados
    b_10000 = 0 # contador de billetes de 10000 entregados
    b_5000 = 0 # contador de billetes de 5000 entregados

    while monto > 0: # mientras quede monto por distribuir
        if monto >= 20000 and billetes_20000 > 0: # si el monto es mayor o igual a 20000 y hay billetes disponibles
            monto -= 20000 # restar 20000 al monto
            b_20000 += 1 # aumentar el contador de billetes entregados en uno
            billetes_20000 -= 1 # disminuir el contador de billetes disponibles en uno
        elif monto >= 10000 and billetes_10000 > 0: # si el monto es mayor o igual a 10000 y hay billetes disponibles
            monto -= 10000 # restar 10000 al monto
            b_10000 += 1 # aumentar el contador de billetes entregados en uno
            billetes_10000 -= 1 # disminuir el contador de billetes disponibles en uno
        elif monto >= 5000 and billetes_5000 > 0: # si el monto es mayor o igual a 5000 y hay billetes disponibles
            monto -= 5000 # restar 5000 al monto
            b_5000 += 1 # aumentar el contador de billetes entregados en uno
            billetes_5000 -= 1 # disminuir el contador de billetes disponibles en uno
    
    return (b_20000, b_10000, b_5000) # devolver una tupla con los contadores de cada denominación

# Definir una función para retirar dinero
def retirar_dinero():
    global saldo_cajero, saldo_cuenta # usar las variables globales de saldos
    monto = int(input("Ingrese el monto a retirar: ")) # pedir el monto al usuario
    if monto > saldo_cuenta or monto > saldo_cajero: # si el monto es mayor que el saldo disponible
        print("Monto no permitido") # imprimir el mensaje de error
        retirar_dinero() # volver a llamar a la función recursivamente
    else: # si el monto es válido
        saldo_cajero -= monto # restar el monto al saldo del cajero
        saldo_cuenta -= monto # restar el monto al saldo de la cuenta
        print("Saldo cuenta: ", saldo_cuenta) # imprimir el nuevo saldo de la cuenta
        print("Saldo cajero: ", saldo_cajero) # imprimir el nuevo saldo del cajero
        b_20000, b_10000, b_5000 = distribuir_monto(monto) # llamar a la función para distribuir el monto y obtener los billetes entregados
        print("Billetes 20000: ", b_20000) # imprimir la cantidad de billetes de 20000 entregados
        print("Billetes 10000: ", b_10000) # imprimir la cantidad de billetes de 10000 entregados
        print("Billetes 5000: ", b_5000) # imprimir la cantidad de billetes de 5000 entregados

# Definir una función principal para ejecutar el programa
def main():
    usuario_ingresado = int(input("Ingrese su usuario: "))
    if usuario_ingresado in usuarios: # si el usuario está en el diccionario
        clave = usuarios[usuario_ingresado] # obtener la clave correspondiente del diccionario
        if validar_clave(clave): # si la clave es válida
            retirar_dinero() # llamar a la función para retirar dinero
            opcion = input("¿Desea realizar otra operación? (N para salir): ") # preguntar si desea continuar
            if opcion.upper() != "N": # si la opción es distinta de N (mayúscula o minúscula)
                main() # volver a llamar a la función principal recursivamente
            else: # si la opción es N (mayúscula o minúscula)
                print("Gracias por usar nuestro servicio") # imprimir el mensaje de despedida
                return # terminar el programa
    else: # si el usuario no está en el diccionario
        print("Usuario inválido") # imprimir el mensaje de error
        main() # volver a llamar a la función principal recursivamente

# Llamar a la función principal para iniciar el programa
main()