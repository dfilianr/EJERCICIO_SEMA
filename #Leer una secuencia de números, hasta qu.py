#Leer una secuencia de números, hasta que se introduce un número negativo y
#mostrar la suma de dichos números.
# num=int(input("Cifras de numeros:"))
# suma= 0 
# while  num > 0 :
#     num= int(input("numeros:")) 
#     suma = suma + sumaDigitos(num)
#     num= num-1 
#     print(suma)   

def sumaDigitos(num) :
    s=0 
    while num > 0:
        s=s +num % 10
        num =num // 10
    return s    
nu=int(input("cantidad de numeros:"))
suma= 0 
while  nu > 0 :
    num= int(input("numeros: ")) 
    suma = suma + sumaDigitos(num)
    nu= nu-1 
    print(suma)     