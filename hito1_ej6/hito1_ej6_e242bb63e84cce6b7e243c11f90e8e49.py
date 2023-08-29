# ingrese un valor de menor a mayor
val_uno= int(input("valor uno:"))
val_dos= int(input("valor dos:"))
val_tres= int(input("valor tres:"))

# valor Menor
val_menor= min(val_uno,val_dos,val_tres)

# valor mayor
val_mayor= max(val_uno,val_dos,val_tres)

#Valor Intermedio
val_inter= (val_uno + val_dos + val_tres)-val_mayor-val_menor

#orden de menor a mayor
print(format(val_menor)+",",format(val_inter)+",",format(val_mayor))