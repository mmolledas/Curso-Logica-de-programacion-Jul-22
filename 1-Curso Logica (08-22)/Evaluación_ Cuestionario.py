#ENTRADA DE DATOS

#PREGUNTAS

aciertos=0      #variable contador      #variables temporales, auxiliares y acumulaodres

pregunta_1 = input("¿Herramienta de programación, parecido al lenguaje español utilizado para crear código?.\n A:IDE  B:Pseudocodigo  C:Compilador    D:ANSI/ISO \n")

if (pregunta_1== "b"):
    aciertos = aciertos + 1

pregunta_2 = input("¿Conjunto de símbolos, letras, números, imágenes, audio y video\n organizadas y que son relevantes en un tiempo y forma determinados.?.\n A:Información  B:Datos  C:Programa   D:Código  \n")

if (pregunta_2== "a"):
    aciertos = aciertos + 1


pregunta_3 = input("¿Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.?\n A:IEEE  B:IDE  C:ANSI/ISO   D:VSCode  \n")

if (pregunta_3== "c"):
    aciertos = aciertos + 1


pregunta_4 = input("¿Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.?\n A:Proceso  B:Solución  C:Función   D:Algoritmo  \n")

if (pregunta_4== "a"):
    aciertos = aciertos + 1


pregunta_5 = input("¿Conjunto de elementos que se relacionan para cumplir una función determinada.?\n A:Estructura  B:Datos  C:Operación   D:Sistema \n")

if (pregunta_5== "d"):
    aciertos = aciertos + 1

pregunta_6 = input("¿Componente de un IDE que se encarga de traducir el código fuente a código máquina.?\n A:Depurador  B:Editor de Texto  C:Terminal de Salida   D:Compilador/Intérprete \n")

if (pregunta_6== "d"):
    aciertos = aciertos + 1


pregunta_7 = input("¿Elemento que se usa para almacenar una cantidad donde cambia su valor?\n A:Constante  B:Variable  C:Librería   D:Tipo de Dato \n")

if (pregunta_7== "b"):
    aciertos = aciertos + 1


pregunta_8 = input("¿Conjunto de símbolos, letras, números que no tienen un significado.?\n A:Datos  B:Estructura  C:Información    D:Sistema \n")

if (pregunta_8== "a"):
    aciertos = aciertos + 1


pregunta_9 = input("¿Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.?\n A:Filosofía  B:Sociología  C:Lógica    D:Argumentación \n")

if (pregunta_9== "c"):
    aciertos = aciertos + 1


pregunta_10 = input("¿ Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.?\n A:Evento  B:Estándar  C:Calidad    D:Productividad \n")

if (pregunta_10== "b"):
    aciertos = aciertos + 1


pregunta_11 = input("¿Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.?\n A:Estructura  B:Sistema  C:Objeto    D:Virtual \n")

if (pregunta_11== "a"):
    aciertos = aciertos + 1


pregunta_12 = input("¿Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.?\n A:Operaciones/Cálculos  B:Sintaxis  C:Programa de Computadora  D:Comando \n")

if (pregunta_12== "a"):
    aciertos = aciertos + 1


Promedio = (aciertos*100)/12 

#Salida de Datos
print("El total de Aciertos es =", aciertos)
print("El promedio es=", Promedio)