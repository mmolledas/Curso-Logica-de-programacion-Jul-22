#CICLO FOR (PARA)  # si queremos incrementar solo ponemos 1 si es decrementar -1

for i in  range(0, 5, 1):  #1er parametro es inicial, condicional final i <5, incremento o decremento
    print(f"{i} -Hola")         #f = formatear

'''

PRUEBA DE ESCRITORIO (simulacion de como trabaja la PC internamente)
    variable    proceso
        i       imprimir      
        1         Hola          
        2         Hola 
        3         Hola
        4         Hola    
        5           

valor inicial

valor final

'''
#####  CICLO WHILE (MIENTRA)

j= 1                    #Valor inicial
while (j <=  10):       # condicion final
    print(j, "hola")       #proceso
    j= j + 1            #incremento / decremetno
