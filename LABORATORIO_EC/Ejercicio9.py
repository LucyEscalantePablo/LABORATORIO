
numero1 = int(input('valor del numero "a": '))
numero2 = int(input('valor del numero "b": '))

def sumaRecur (numero2):
    if numero2 == 1:
        return 1
    return  1 + sumaRecur( numero2-1)
    

resultado = sumaRecur(numero2)
print(resultado + numero1)