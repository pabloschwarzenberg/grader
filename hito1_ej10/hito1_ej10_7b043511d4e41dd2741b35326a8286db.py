'''
Tu cajero debe pedir un usuario y una clave para ingresar.
Al principio debe tener 1.000.000 como saldo inicial.
Tu cajero debe dejar ingresar al usuario 10334151 con la clave 1803, quien tiene al inicio del programa 100.000 en su cuenta.
Lo único que se puede hacer en este nivel es retirar dinero de la cuenta corriente.
Tu programa debe validar la clave y el monto a retirar, indicando el mensaje “clave invalida” cuando la clave no corresponde y al tercer intento fallido debe indicar “tarjeta bloqueada” y salir del programa.
Si la clave es válida, debe preguntar por el monto a retirar.
Cuando se hace el retiro de un monto que no es válido debe indicar “monto no permitido”, si el monto se puede retirar debe actualizar los saldos e imprimir el nuevo saldo que quedó en la cuenta corriente y el cajero.
Por ejemplo al retirar 45.000 debiera imprimir:
saldo cuenta=55000
saldo cajero=955000
Tu programa debe repetirse continuamente, para salir la persona debe ingresar algo distinto a la letra “N”.
'''
def showBalance(accountBalance, atmBalance):
    print("saldo cuenta="+str(accountBalance))
    print("saldo cajero="+str(atmBalance))

def applyWithdraw(amount, atmBalance, accountBalance):
    atmBalance -= amount
    accountBalance -= amount
    return atmBalance, accountBalance

def validateWithdraw(accountBalance, atmBalance):
    amount = int(input("Cantidad a retirar: "))
    while(str(amount).isnumeric() == False):
        amount = int(input("Cantidad a retirar: "))
    validAmount = False
    while(not(amount < accountBalance) or not (amount < atmBalance)):
        amount = int(input("Error, ingrese una cantidad valida: "))
    else:
        return amount

def askForCredentials(errorCounter):
    user = checkInput("usuario")
    password = checkInput("contraseña")
    while(user != 10334151):
        user = checkInput("usuario")
    else:
        while(password != 1803):
            password = int(input("clave invalida"))
            errorCounter += 1
        else:
            valid = True
    return user, password, errorCounter

def checkInput(msg):
    credential = str(input("Ingrese su "+ msg +": "))
    while(not credential.isnumeric()):
        credential = input("Error, intente nuevamente con su "+ msg +": ")
    else:
        return credential

selection = "N"
accountBalance = 100000
atmBalance = 1000000
errorCounter = 0
while(selection == "N"):
    user, password, errorCounter = askForCredentials(errorCounter)
    amount = validateWithdraw(accountBalance, atmBalance)
    atmBalance, accountBalance = applyWithdraw(amount, atmBalance, accountBalance)
    showBalance(accountBalance, atmBalance)
else:
    print( )