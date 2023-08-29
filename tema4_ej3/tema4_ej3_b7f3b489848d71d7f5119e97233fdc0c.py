def jerigonzo(string):
    traducidooo = []
    for palabraa in string:
        for letrass in palabraa:
            if letrass in "aeiouAEIOU":
                letrass = letrass + "p"+ letrass
            traducidooo.append(letrass)
    traducidooo = "".join(traducidooo)
    return traducidooo
         