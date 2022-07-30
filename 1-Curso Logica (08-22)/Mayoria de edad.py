#MANEJO DE ERRORES O EXCEPCIONES
try:
    edad= int(input("escribe tu edad: "))

    if(edad>=18):
        print("mayor de edad")

    elif(edad<18):
        print("menor de edad")

    else:
        print("error")
except:
    print("invalido)