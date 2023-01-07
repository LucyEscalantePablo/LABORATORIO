nombre = []
longitudNom = []

tamañoArreglo = int(input('ingrese el tamaño del arreglo: '))

for i in range (tamañoArreglo):
    nom = input('Ingrese el nombre: ')
    nombre.append(nom)
    contamosLong = len(nom)
    longitudNom.append(contamosLong)

print(nombre)
print(longitudNom)