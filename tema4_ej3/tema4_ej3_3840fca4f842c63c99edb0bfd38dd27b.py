palabra = ""
for letra in string:
    palabra += letra
    if letra.lower() in "aeiou":
       palabra += "p" + letra
return
mensaje= jerigonzo('ni un brillo pelao')
print(mensaje)
         