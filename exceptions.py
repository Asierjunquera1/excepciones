import re

def pedir_correo():
    print("Introduzca su dirección de correo electrónico:")
    correo = input("->")
    while True:
        es_un_correo= re.search(".+@.+\..+", correo)
        if es_un_correo!=None:
            if correo.endswith("eni.es"):
                print("¡Bienvenido {}!".format(correo.split('@')[0]))
            else:
                print("Cuenta bloqueada a causa de un ataque")

            break

        elif correo=="" or correo==" ":
            print("Es una entrada incorrecta. Introduzca una dirección de correo electrónico: ")
            correo = input("->")

        elif es_un_correo==None:
            print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx. Introduzca una dirección de correo electrónico: ")
            correo = input("->")
            es_un_correo= re.search(".+@.+\..+", correo)
        

        
        

pedir_correo()
