#Ejercicio4

#Entrada de Datos

grados= float(input("indicar los grados:") )
kelvin= float(273.15)
fahrenheit= float(32)

# PROCESO

celcius_a_kelvin= grados+kelvin
celcius_a_fahrenheit1= (grados*1.8)+fahrenheit
celcius_a_fahrenheit2= (9*grados/5)+fahrenheit 

fahrenheit_a_celcius= ((5*(grados-32)/9))
fahrenheit_a_Kelvin= ((5*(grados-32)/9)+kelvin)

kelvin_a_celcius= (grados-kelvin)
kelvin_a_fahrenheit= ((9*(grados-kelvin)/5)+fahrenheit)

#SALIDA DE DATOS

print("celcius a kelvin es=", celcius_a_kelvin)
print("celcius a fahrenheit es=", celcius_a_fahrenheit1)
print("celcius a fahrenheint es =", celcius_a_fahrenheit2)

print("fahrenheit a celcius es=", fahrenheit_a_celcius)
print("fahrenheit a kelvin es=", fahrenheit_a_Kelvin)

print("kelvin a celcius es=", kelvin_a_celcius)
print("kelvin a fahrenheit es=", kelvin_a_fahrenheit)