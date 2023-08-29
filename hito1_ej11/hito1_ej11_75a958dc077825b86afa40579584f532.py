#Cajero Automático
salarioactual=eval(input("salario actual: "))
if salarioactual>=0 and salarioactual<=9000:
    print("su nuevo salario es de ",salarionuevo)
elif salarioactual>=9001 and salarioactual<=15000:
    print("su nuevo salario es de ",salarionuevo)
elif salarioactual>=15001 and salarioactual<=20000:
    print("su nuevo salario es de ",salarionuevo)
elif salarioactual>20000:
    print("su nuevo salario es de ",salarioactual)
else:
    print("su salario no puede ser negativo")