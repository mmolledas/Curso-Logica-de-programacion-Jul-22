##Calculo de Nomina
##entrada de datos
jornada= int(input("coloque la jornada del trabajador"))
sueldo_diario= float(input("coloque su sueldo diario"))
faltas= int(input("colocar el número de faltas en el mes"))
horas_extras= int(input("coloque el numero de hrs extras realizadas"))

#PROCESO
#PERCEPCIONES
sueldo_mensual= sueldo_diario*30
hrs_extras = sueldo_diario/jornada*horas_extras
bono=0
if faltas==0:
    bono=sueldo_mensual*.30
elif faltas>0 and faltas==1:
    bono= sueldo_mensual*.15

elif faltas>1:
    bono= 0

total_percepciones= (sueldo_mensual+hrs_extras+bono)

#Descuentos
isr= (sueldo_diario*30)*0.16
imss= 80
afore= 200
descuento_por_faltas= faltas*sueldo_diario 
total_descuentos= isr+imss+afore+descuento_por_faltas

#Pago
pagar= total_percepciones-total_descuentos

##SALIDA DE DATOS
print("Percepciones")
print("Sueldo Mensual=\t\t", sueldo_mensual)
print("Horas Extra=\t\t", hrs_extras)
print("Bonos=\t\t\t", bono)
print("Total de Percepciones=\t", sueldo_mensual+hrs_extras+bono)

print("Descuentos")

print("ISR=\t\t", isr)
print("IMSS=\t\t", imss)
print("Afore=\t\t", afore)
print("faltas=\t\t", descuento_por_faltas)
print("Total Descuentos=\t", total_descuentos)

print("Total a Pagar=", pagar )