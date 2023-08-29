#Aprobación de créditos

Ing= int(input("Ingrese su ingreso mensual"))
Eda= int(input("Ingrese su edad"))
while not(Eda<=110 and Eda>=1):
    Eda= int(input("Ingrese una edad valida"))
Hijos= int(input("Ingrese numero de hijos"))
while not(Hijos>=0):
    Hijos= int(input("Ingrese numero de hijos valido"))
Permanencia=int(input("Ingrese años en el banco"))
while not(Permanencia>=0):
    Permanencia= int(input("Ingrese numero de años valido"))
Estado= str(input("Ingrese un S si es soltero o un C si es casado"))
while not(Estado==S or Estado==C):
    Estado= str(input("Ingrese una S si es soltero o una C si es casado"))
