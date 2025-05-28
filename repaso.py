import time

# nombre = "Lucas"
# time.sleep(1)
# edad = 18
# time.sleep(1)
# print("Hola, mi nombre es", nombre, "en 5 años tendras ", edad+5, "años.")


# n1=int(input("ingrese un numeros: "))

# n2=int(input("ingrese otro numeros: "))

# suma=n1+n2
# print("la suma es ", suma)

# if suma>10:
#     print("El numero es mayor de que 10")
# elif suma<10:
#     print("El numero es menor de que 10")
# else:
#     print("El numero es igual a 10")


# for i in range(3):
#     print("Repeticion ",i+1)
#     time.sleep(1)


# num=8

# for i in range(10):
#     print(num , "x", i+1, "=", num*(i+1))


# Ejercicio 1

# cantArt=0
# total=0

# while True:
#     while True:
#         try: 
#             print('''
#                   Seleccione una opción:
#                   1. Teclados
#                   2. Monitores
#                   3. Audífonos
#                   4. Salir
#                   ''')
#             op=int(input())
#             break
#         except Exception:
#             print("Ingrese numeros enteros")

#     match op:
#         case 1:
#             total+=20000
#             cantArt+=1
#         case 2:
#             total+=40000
#             cantArt+=1
#         case 3:
#             total+=80000
#             cantArt+=1
#         case 4:
#             break
#         case _:

#############################################################################################################################

# Ejercicio 2

# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.


# print("Bienvenido al sistema de pago de tarjeta de crédito")
# print("Su saldo inicial es de $100.000")
# saldo=100000
# while True:
#     while True: 
#         print('''
#               Seleccione una opción:
#               1. Realizar un pago
#               2. Simular compras
#               3. Salir
#               ''')
#         op=int(input())
#         break
#     match op:
#         case 1:
#             while True:
#                 try: 
#                     pago=int(input("Ingrese el monto a pagar: "))
#                     if pago<0:
#                         print("El monto a pagar no puede ser negativo")
#                         continue
#                     if pago>saldo:
#                         print("El monto a pagar no puede exceder el saldo actual")
#                         continue
#                     saldo-=pago
#                     print(f"Pago realizado. Su nuevo saldo es de ${saldo}")
#                     break
#                 except Exception:
#                     print("Ingrese un monto válido")
#         case 2:
#              while True:
#                 try: 
#                     compras=int(input("Ingrese el monto de la compra: "))
#                     if compras<0:
#                         print("El monto de la compra no puede ser negativo")
#                         continue
#                     saldo-=compras
#                     print(f"Compra realizada. Su nuevo saldo es de ${saldo}")
#                     break
#                 except Exception:
#                     print("Ingrese un monto válido")
#         case 3:
#             print("Saliendo del sistema...")
#             break
#         case _:
#             print("Opción no válida. Intente nuevamente.")

# Mejorar en crear usuario (opcional), tambien agregar menu de comnpras (No estoy seguro si es necesario)

#############################################################################################################################

# Ejercicio 3 (EVALUACIÓN FORMATIVA)


print("Bienvenido a nuestra tienda de sushi")

while True:
    while True: 
        print('''
              Seleccione nuestras siguientes opciones:
              1. Registrar cliente
              2. Loggin
              3. Compras de sushi
              4. Salir
              ''')
        op=int(input())
        break
    match op:
        case 1:
            while True:
                try: 
                    nombre= nombre.isalpha (input("Ingrese su nombre: "))

                except Exception:
                    print("Ingrese un nombre válido")
            
            while True:
                try: 
                    apellido=input("Ingrese su apellido: ")
                except Exception:
                    print("Ingrese un apellido válido")

# Resolver en la mojo dojo house
