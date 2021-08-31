#Leer un número y mostrar su tabla de multiplicar.
n= int(input("ingrense un numero positivo:"))
if n > 0:
    for i in range(1,11):
        print(n,"x", i ,"es igual a:", n*i )
else :
    print("El numero ingresado no es valido ")        