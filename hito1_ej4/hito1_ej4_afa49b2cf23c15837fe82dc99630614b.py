numero=int(input("ingrese numero :"))
division=1
rest="0"
while division!=0:
    resto=str(numero%2)
    division=numero//2
    numero=division
    
    rest+=resto
    
print("resultado",rest[1:len(rest)])

