def decodificar(mensaje):
    car_bin = mensaje.split(",")
    car_dec = []
    car_asc = []
    for car in car_bin:
        suma = 0
        for i in range(8):
            suma += int(car[7-i])*2**(i)
        car_dec.append(suma)
    for car in car_dec:
        car_asc.append(chr(car))
    return "".join(car_asc)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
         