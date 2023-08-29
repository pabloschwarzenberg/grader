def jerigonzo(s):
    vocales=['a','e','i','o','u','A','E','I','O','U'] 
    for vocal in vocales: 
        s=s.replace(vocal,vocal+"p"+vocal) 
    return s

if __name__ == "__main__":
    pass