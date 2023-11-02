

hobbies = open("miHobbieFavoritos.txt", "w")

dato_1 = input("Ingrese su primer Hobbie: ")
dato_2 = input("Ingrese su segundo Hobbie: ")
dato_3 = input("Ingrese su tercer Hobbie:")

hobbies.write(dato_1 + '\n')
hobbies.write(dato_2 + '\n')
hobbies.write(dato_3 + '\n')

hobbies.close()

print("HOBBIES GUARDADOS")





