#EJERCICIO 2 CIRCULO
#libreria
import math
#DECLARAR DATOS
#AREA= PI x Radio al cuadrado
#perimetro=2*PI*RADIO

radio= float(input("indicar el radio del circulo: "))
PI= math.pi  

#PROCESOS
area = PI* pow(radio, 2)
perimetro= 2*PI*radio

#SALIDA DE DATOS
print("el area del circulo es =", round(area, 3))
print("el perimetro del circulo es =", round(perimetro, 3))
