print("Kevin" + "1995" + "Hdez")


edad = 27


if edad > 18:
    print("Es mayor de edad")
    print("Es mayor de edad")
    print("Es mayor de edad")
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    print("Es menor de edad")
    print("Es menor de edad")
    print("Es menor de edad")


lista_del_mago = ["Patas de araña", "Lengua de rana", "Ojo de buey", "Ala de murciélago"]

print(lista_del_mago[0])
print(lista_del_mago[1])
print(lista_del_mago[2])
print(lista_del_mago[3])


for elemento in lista_del_mago:
    print(elemento)

palabra = "elefante"

acumulador = 0

for letra in palabra:
    if letra == "e":
        acumulador = acumulador + 1
    
print(palabra + str(acumulador))

