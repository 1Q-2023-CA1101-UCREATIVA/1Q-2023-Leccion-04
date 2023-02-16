palabra = "kevin"

for letra in palabra:
    print(letra + 'h' + 'r')

marcas = ["BMW", "Honda", "Nissan"]

for marca in marcas:
    print(marca)

indice = 0
for marca in marcas:
    print(indice, marca)
    indice = indice + 1

indice = 0
for letra in palabra:
    print(indice, letra)
    indice = indice + 1


for indice, letra in enumerate(palabra):
    print(indice, letra)

