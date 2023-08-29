def jerigonzo(string):
    jer=""
    for l in range(len(string)):
       if string[l] in "aeiou":
         jer+=string[l]+"p"+string[l]
       else:
         jer+=string[l]
    return jer  