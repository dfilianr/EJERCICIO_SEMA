#Dado un número mostrar su valor en binario.
def binarios (num):
    num =0
num=int(input("Ingrese numero: "))
lista= [ ] 
while num >=1:
    lista.insert(0,num%2) 
    num = num//2
resultado= "".join(str(i)for i in lista)   

print (resultado)