#EJERCICIO 1 PROMEDIO
#ENTRADA DE DATOS
#DECLARAR DATOS


try:

  calificacion_1= float(input("escribir 1er calificacion: "))
  calificacion_2= float(input("escribir 2da calificacion: "))
  calificacion_3= float(input("escribir 3era calificacion: "))

  promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

  if promedio==0 or promedio <=5.9:
    print("Reprobado")

  elif promedio==6:
    print("pansaso")

  elif promedio>6 or promedio==10:
    print("aprobado")

  else:
    print("promedio invalido")
except:
  print("Error")





  




#"APROBADO  ENTRE 6 Y 10"
#"PANSASO EQUIVALENTE  A 6"
#"REPROBADO ENTRE 0 Y 5.99"
#"PROMEDIO IVALIDO"