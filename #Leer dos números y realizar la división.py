#Leer dos números y realizar la división mediante restas mostrando el cociente y el
#resto.
def cocien_res__divi (numerador,denominador):
    cociente= 0
    resto =0

    while numerador >= denominador:
        numerador -=denominador 
        resto=numerador
        cociente += 1 
    return  (cociente, resto)

resultado =cocien_res__divi(12,4)
print(resultado)     