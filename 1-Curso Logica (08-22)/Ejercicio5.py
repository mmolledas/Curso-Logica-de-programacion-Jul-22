#FORMULA GENERAL
import math
#ENTRADAD DE DATOS
a=  float(input("esciba el valor de a:") )
b=  float(input("esciba el valor de b:") )
c=  float(input("esciba el valor de c:") )

#PROCESO



x1= (-b-pow(pow(b,2)-4*a*c,1/2))/(2*a)

x2= (-b+ pow(pow(b,2)-4*a*c,1/2))/(2*a)

#SALIDA DE DATOS

print("x1 es=", x1)
print("x2 es =",x2)
