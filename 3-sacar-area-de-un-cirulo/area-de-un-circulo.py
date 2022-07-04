#Construye un programa que al recibir como dato el radio de un circulo, calcule e imprima tanto su area como la longitud de su circunferencia

#el area de un circulo la calculamos como 
#area = pi * radio^2

#la longitud de la circunferencia del ciculo la calculamos de la siguiente forma
# longitud = 2 * pi * radio

import math

print("Este es un programa para sacar el area y perimetro de un circulo")

radio = float(input("Introduce cuanto mide el radio del circulo: "))

area = (math.pi * math.pow(radio, 2))
longitud = (2 * round(math.pi, 4) * radio)

print("El area del circulo de radio %s es de %s y el perimetro es de %s" %(radio, round(area, 4),round(longitud, 4))) 
