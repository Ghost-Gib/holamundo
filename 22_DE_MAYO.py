#Ejercicios de for 

#Perros de caza
# Pida al usuario la cantidad de perros
# Muestre cual es la cuota minima de conejos
# luego consulte cuantos conejos trajo
# si el perro trajo la cantidad minima
#cumplio la cuota, sino, se queda sin filete
#mostrar resumen de perro que cumplieron y los que no

# Ejercicio 1 HECHO POR MIIIII
import random
print("Ingrese la cantidad de perros")
perros = int(input())
perros_que_cumplieron = 0
perros_que_no_cumplieron = 0
for i in range(perros):
    print("Ingrese la cuota minima de conejos")
    cuota_minima = int(input())
    print("Ingrese la cantidad de conejos que lograron traer")
    conejos = int(input()) # random.randint(1, 10)


    if conejos >= cuota_minima:
        perros_que_cumplieron += 1
        print("El perro cumplio la cuota")
    else:
        perros_que_no_cumplieron += 1
        print("El perro no cumplio con la cuota")
        print("No tiene premio")

print("Resumen de perros que cumplieron la cuota:", perros_que_cumplieron)
print("Resumen de perros que no cumplieron la cuota:", perros_que_no_cumplieron)

        