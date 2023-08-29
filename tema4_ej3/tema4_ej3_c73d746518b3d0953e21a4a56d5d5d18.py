def jerigonzo(string):
    libro = string
    vocales=["a","e","i","o","u"]
    conversion_1 =""
    for i in libro:

        conversion_1 = conversion_1 + i
        if(i in vocales):
            conversion_1 = conversion_1 +"p"+i
    return conversion_1
         