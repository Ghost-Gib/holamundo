# Ejercicio 1
# CONTABILIDAD DE LA EMPRESA
#           1) Ingresar nombre
#           2) Visualizar nombres
#           3) Visualizar años de antiguedad
#           4)Salir
empleados = []
edad = []
a_antiguedad = []
while True:
    print ('''Bienvenido, ES HORA DE REGISTRARNOS
     1.- Registrar tu usuario
     2-. Ver nombres Registrados
     3.- Ver años de antiguedad
     4.- Salir''')
    try:
        op = int(input("Ingrese una opcion: "))
    except ValueError:
        print ("Opcion no valida cueck cueck...")
    match op:
        case 1:
            nombre = (input("Ingrese su nombre: "))
            empleados.append(nombre)
            print (f"Su nombre ingresado es: {nombre}")
            edades = (input("Ingrese su edad: "))
            edad.append(edades)
            print(f"Su edad registrada seria: {edades}")
        case 2:
            print ("Ahora vera los usuarios que se registraron")
            print (f'''Empleados registrados: 
                   Nombre: {empleados}
                   Edad: {edad}''')
        case 3:



# Ejercicio 2

# Estrella=0
# Entradas=50
# Entradas_c=0


# while True:
#         print ("Bienvenido al sistema de venta de entradas del Cine Estrella \n 1) Ver cuantas entradas quedan \n 2) Comprar una cantidad de entradas \n 3) Salir del sistema")
#         try:
#             Estrella=int(input("Elija su opcion: "))
#         except ValueError:
#             print ("Debe ingresar un número entero que sea valido")
#         if Estrella == 1:
#             print(f"Entradas disponibles: {Entradas}")
#             print ("Volviendo al Menu Principal...")
#         elif Estrella == 2:
#             Entradas_c=int(input("Seleccione las entradas que desea comprar: "))
#             Entradas-=Entradas_c
#             print(f"Compra exitosa, las entradas disponibles son: {Entradas}")
#         elif Estrella == 3:
#             print ("Gracias por usar el sistema de ventas del Cine Estrella ¡Hasta la proxima!")
#             break
#         else:
#             print("Ingrese una opccion valida")
