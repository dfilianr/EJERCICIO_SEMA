#LETRA DE UN APARTAMENTO
EDIFICIO=input("ingrese el nombre del edificio:")
print("su edificio es :", EDIFICIO )
apartame=input("ingrese caracter:")
print("su apartamento es :", apartame)
frase= apartame
conteo= { }
for letra in frase.lower():
    if letra not in conteo :
       conteo[letra] =1
    else :
        conteo [letra] += 1
for k , v in conteo.items():
    print("{}:{}".format(k,v))

