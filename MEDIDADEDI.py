#calcular la altura de un edificio
import math
som= float(input("valor : "))
alfa=int(input("angulo : "))
alfa = math.radians(alfa)
h = som*math.tan(alfa)
print("la atura es ",round(h,1),"mtr")