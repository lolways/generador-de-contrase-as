import random

chars = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ1234567890!#$%&/()=?¡¿,."

while 1:
    contraseña_lon= int(input("¿Que largo necesitas que la contraseña sea?: "))
    
    contraseña_cantd= int(input("¿cuantas contraseñas necesitas?: "))
    
    for x in range(0, contraseña_cantd):
        print(x)
        contraseña = ""
       
        for  x in range(0, contraseña_lon):
            contraseña_char = random.choice(chars)
            contraseña      = contraseña + contraseña_char
       
        print("Aca esta su contraseña: ", contraseña)
        
        archivo = open("contraseñas.txt", "w")

        nc = input("para que es su contraseña: ")

        archivo.write(nc + ":" + contraseña)

        archivo.close()
    exit()





