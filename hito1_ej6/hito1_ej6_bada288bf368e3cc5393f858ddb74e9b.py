nu1= input("Escriba un numero ")
nu2= input("Escriba un segundo numero ")
nu3= input("Escriba un tercer numero ")
if nu1 > nu2 > nu3:
    print(f'{nu1},{nu2},{nu3}')
if nu2 > nu1 > nu3:
    print(f'{nu2},{nu1},{nu3}')
if nu3 > nu2 > nu1:
    print(f'{nu3},{nu2},{nu1}')
if nu3 > nu1 > nu2:
    print(f'{nu3},{nu1},{nu2}')
if nu1 > nu3 > nu2:
    print(f'{nu1},{nu3},{nu2}')
if nu2 > nu3 > nu1:
    print(f'{nu2},{nu3},{nu1}')
if nu1 == nu2 and nu1 > nu3:
    print(f'{nu1},{nu2},{nu3}')
if nu1 == nu3 and nu1 > nu2:
    print(f'{nu1},{nu3},{nu2}')
if nu1 == nu2 and nu1 < nu3:
    print(f'{nu3},{nu2},{nu1}')