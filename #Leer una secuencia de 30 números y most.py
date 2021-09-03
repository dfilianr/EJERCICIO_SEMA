#Leer una secuencia de 30 números y mostrar la suma y el producto de ellos.
lista= [20,100 ]
def sumar(lista):      
   if lista== [ ]: 
    suma =0
   else:
       suma= lista [0]+ sumar (lista[1:])
   return suma 
print(sumar(lista))

  
def multiplicar(numeros):
    producto = 1

    for n in numeros :
        producto*=n
    return producto  
print(multiplicar(lista))
  