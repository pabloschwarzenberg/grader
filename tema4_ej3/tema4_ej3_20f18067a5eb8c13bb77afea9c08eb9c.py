def jerigonzo(string):
    a='a'
    e='e'
    i='i'
    o='o'
    u='u'
    letra=0
    largo=len(string)
    text=''
    while letra<largo:
        if a in string[letra]:
            text=text+string[letra]+"pa"
        elif e in string[letra]:
            text=text+string[letra]+"pe"
        elif i in string[letra]:
            text=text+string[letra]+"pi"
        elif o in string[letra]:
            text=text+string[letra]+"po"
        elif u in string[letra]:
            text=text+string[letra]+"pu"
        else:
            text=text+string[letra]
        letra=letra+1
    return text

if __name__ == "__main__":
    pass
         