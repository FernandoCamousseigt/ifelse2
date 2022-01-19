import sys

W = float(sys.argv[1])
H = float(sys.argv[2])/100

IMC = W/H**2     

print("Su IMC es:",round(IMC,2))

if IMC < 18.5:
    clas = "Bajo Peso"
elif IMC >= 18.5 and IMC < 25:
    clas = "Adecuado"
elif IMC >= 25 and IMC < 30:
    clas = "Sobrepeso"
elif IMC >= 30 and IMC < 35:
    clas = "Obesidad Grado I"
elif IMC >= 35 and IMC < 40:
    clas = "Obesidad Grado II"
else:
    clas = "Obesidad Grado III"

print("La clasificación OMS es",clas)



"""
W : corresponde al peso de la persona en Kg.
H: corresponde a la altura en metros.
IMC: EL valor del IMC, en [Kg/m2]
"""
# operator ** = Exponentiation

#python file.py argv1 argv2
#python imc.py 81 178
    