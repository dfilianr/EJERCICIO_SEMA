#Constante y variables
#variable1 = 23
#variable2 = 12
#suma = variable1 + variable2
#print("la suma de ",variable1,"+",variable2,"=",suma)
#iva = 0.12
#calcular = suma * iva
#total= suma+ calcular
#print("El iva de la suma es:", total)
#CALCULAR LA EDAD DE UN NIÑO

#from datetime import date
#def calcular_edad (fecha_naci):
 #   fecha_actu = date.today()
  #  calculo = fecha_actu.year - fecha_naci.year

   # return calculo
#fecha_naci_santi = date(2002,10,21)
#edad= calcular_edad(fecha_naci_santi)
#print("la edad de santi es",edad)

#import math
#som= float(input("valor : "))
#alfa=int(input("angulo : "))
#alfa = math.radians(alfa)
#h = som*math.tan(alfa)
#print("la atura es ",round(h,1),"mtr")

#print("INGRESA TU NOMBRE ")
#nombre= input()
#print("INGRESA TU Apellido  ")
#apellido= input()
#print("el nombre ingresado es: " ,nombre)
#print("el apellido ingresado es: " ,apellido)

#LETRA DE UN APARTAMENTO
#EDIFICIO=input("ingrese el nombre del edificio:")
#print("su edificio es :", EDIFICIO )
#apartame=input("ingrese caracter:")
#print("su apartamento es :", apartame)
#frase= apartame
#conteo= { }
#for letra in frase.lower():
    #if letra not in conteo :
      # conteo[letra] =1
    #else :
        #conteo [letra] += 1
#for k , v in conteo.items():
    #print("{}:{}".format(k,v))


#TIENE HIJOS O NO
#Nombre = input("ingrese su nombre")
#print("su nombre es :", Nombre)
#hijos= input("tiene hijos ")
#respu = { }
#if respu :
    #print("usted tiene hijos")
#else:
    #print("Usted no tiene hijos ")

class Matriz:
    def __init__(self,matriz):
        self.matriz = matriz
    def mostrar(self):
        for fila in range(len(self.matriz)):
            print(self.matriz[fila])


num=[[10,20,30],[10,20,30,40,23],[11,20,30],[11,20],[11,13,14,15,1620,30],[1,2,3]]
mat= Matriz(num)
mat.mostrar()