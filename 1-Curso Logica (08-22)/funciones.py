#funciones: tareas o acciones(verbos: terminan en ar, er, ir) a ejecutar
#sintaxis
#una funcion se encarga de una sola tarea esto es buena practica
#def nombre_ funcion (parametros o Argumentos)
    #contenido de la funcion 

#DECLARAR FUNCIONES
def Sumar (a, b):   #se obtienen o reciben dos parametros, que sea descriptiba si es suma entonces suma
    return a + b    #retur, retomar, regresar

def Restar (x, y, z):
    return x - y - z

def Rest (d, f, k):         #esta es otra forma de realizar la sintaxis en la salida de datos ya no imprimo solo convoco
    rest1= d - f - k
    print("la resta es =",rest1)

def Dividir (a, b):
    return a / b

def Multiplicar (a, b):
    return a * b


#MANDAR A LLAMAR

suma = Sumar(10, 5)  # se le llamada enviar o pasar los parametros
    #aunque no es necesario invocar los 3 parametros como buena practica se sugiere se indiquen todos los parametros
rest = (20, 3, 0)

división= Dividir(10, 5)
multiplicación= Multiplicar(10, 5)

# SALIDA DE DATOS

print("la suma es =", suma)
print("la resta es=", Restar(20, 3, 0))
print("la división es =", división)
print("la multiplicacon es =", multiplicación)
