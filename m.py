#CALCULAR LA EDAD DE UN NIÑO
from datetime import date
def calcular_edad (fecha_naci):
    fecha_actu = date.today()
    calculo = fecha_actu.year - fecha_naci.year

    return calculo
fecha_naci_santi = date(2002,10,21)
edad= calcular_edad(fecha_naci_santi)
print("la edad de santi es",edad)
