multiplos = []

longitudA = int(input('Ingrese la longitud del array: '))
numero = int(input('Ingrese el número que desea saber sus multiplos: '))

for i in range (longitudA):
    resultado = i*numero
    multiplos.append(resultado)

print(multiplos)