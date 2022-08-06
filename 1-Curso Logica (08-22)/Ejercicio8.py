# ejercicios condiciones y ciclos


#entrada de datos

numero = int(input("indicar un número"))

if  numero <= -1 and numero >-100:
    for numero in range(-1, -101, -2):
        print(numero,)

elif numero >= 0 and numero <100:
    for numero in range(2, 102, 2):
        print(numero,)

else:
    print("No valido")