
# Online Python - IDE, Editor, Compiler, Interpreter
datos=str(input("Ingrese un numero de hasta 4 digitos: "))

if(len(datos)==1):
    print(datos[0],"U",sep="")
elif(len(datos)==2):
    print(datos[0],"D"," + ",datos[1],"U",sep="")
elif(len(datos)==3):
    print(datos[0],"C"," + ",datos[1],"D"," + ",datos[2],"U",sep="")
elif(len(datos)==4):
    print(datos[0],"M"," + ",datos[1],"C"," + ",datos[2],"D"," + ",datos[3],"U",sep="")
