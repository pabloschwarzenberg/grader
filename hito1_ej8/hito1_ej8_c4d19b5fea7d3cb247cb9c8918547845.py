#Descomponer un número
num = int(input("Ingrese numero="))
ter = str(num)
if(len(ter) == 4):
    st1 = int(ter[0])
    st2 = int(ter[1])
    st3 = int(ter[2])
    st4 = int(ter[3])
    print(st1,"M", "+", st2,"C", "+", st3,"D", "+" ,st4,"U")
    
elif(len(ter) == 3):
    st1 = int(ter[0])
    st2 = int(ter[1])
    st3 = int(ter[2])
    print(st1,"C" ,"+", st2,"D", "+", st3,"U")
    
elif(len(ter) == 2):
    st1 = int(ter[0])
    st2 = int(ter[1])
    print(st1,"D", "+" ,st2,"U")

elif(len(ter) == 1):
    st1 = int(ter[0])
    print(st1,"U")      