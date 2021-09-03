#Lee una secuencia de números y determina cual es el mayor de ellos.
lista =[ ]
tamanio = int(input("Tamanio:"))
mayor=0
i=1
while (tamanio > 0):
   numero=int(input("Numero " +str(i) +":")) 
   lista.append(numero)
   i=i+1
   tamanio= tamanio-1
mayor = max(lista)  
print("Lista:",lista)
print("Mayor:",mayor)