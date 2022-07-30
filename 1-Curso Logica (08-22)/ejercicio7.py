#Declarar variables ejercicio Cisterna

#Entrada de datos
#variables


#Proceso Condicionales
try:
    volumen_de_agua= float(input("indicar el volumen de agua en metros:"))
    
    if volumen_de_agua<0:
        print("Fuga en Cisterna")

    elif volumen_de_agua==0:
        print("Encender Bomba de Agua")

    elif volumen_de_agua>=0 and volumen_de_agua <=2:
        print("acelerar bomba de agua")

    elif volumen_de_agua>2 and volumen_de_agua <=4:
        print("bomba trabajando")

    elif volumen_de_agua>4 and volumen_de_agua <6:
        print("Desacelerar Bomba")

    elif volumen_de_agua==6:
        print("Apagar Bomba")

    elif volumen_de_agua>6:
        print("Desbordamiento de agua en Cisterna")

    else:
        print ("llamar al reparador")

except:
    print("error")




