    # Leer 2 números y determinar el mayor de ellos.
mayor= None
for i in range (3):
    n=int(input("ingrense los valores:"))
    if mayor is None or n > mayor:
        mayor= n    
print("El numero mayor es :", mayor)     
 
