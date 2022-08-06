#ARREGLOS EN PYTHON SON LISTAS
#Colección o conjuntos de valores de uno o mas tipos de datos
#la sintaxys es parecido a una valiable:
# nombre arreglo de lista= elementos/ valores

#declarar variables

nombre = ["Mario", "Eduardo", "Alejandra"]
edades = [29, 30, 15]
arreglo_lista = ["Hola", 20, 3.7, True]

#OPERACIONES CON ARREGLOS

#Modificar un elemento
nombre[0]="Mario Alberto"
edades[2]=16
arreglo_lista[3]= False

#agregar un nuevo elemento al arreglo
nombre.append("Paola")
edades.append(18)
arreglo_lista.append("Adios")

#Ordenar los elementos del arreglo A-Z

nombre.sort() #como es tecto ordena de ABC
edades.sort()

#Ordenar los elementos del arreglo Z-A
nombre.reverse() #como es texto ordena de ABC
edades.reverse()

#eliminar elementos del arreglo

nombre.pop(1)

#vaciar o limpiar arreglos
nombre.clear()

#salida de Datos
print(nombre)
print(edades)
print(arreglo_lista)
