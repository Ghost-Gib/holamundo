# EJERCICIO 1

# Ejecutar = str(input("Se ejecutara el lavamanos: "))
# Agua = False

# if Ejecutar == "Si":
#     Agua = True
#     print ("Se realizara la ejecución ahora mismo")
#     print ("El agua esta cayendo")
# elif Ejecutar == "No":
#     Agua = False
#     print ("Vuelva cuando quiera")
# else:
#     print ("Lavese las manos es un sucio")

# EJERCICIO 2 

# import time
# Ejecutar = str(input("Desea prender la luz?: "))
# Luz = False

# if Ejecutar == "Si":
#     Luz = True
#     print ("Se hizo la luz")
#     print ("Explota el techo")
# elif Ejecutar == "No":
#     Luz = False
#     print ("Aparecera...")
#     time.sleep(3)
#     print ("FOXY!!!")
#     time.sleep(1)
#     print ("Mueres por un Jampscure")
# else:
#     print ("Aprenda a escribir mamaguevazo")

# EJERCICIO 3


# import time
# Cafe = False
# Person = str(input('''"Una Persona esta tomando el café:
#     ("Esa persona te esta mirando un buen rato...")               
#     ("Ryuk: Vaya, vaya, un humano tomando el café conm intenciones sospechosas hacia ti")
#     Ryuk: Deseas usar este cuaderno? Escribe su nombre y veras que sucede...: '''))
# time.sleep(2)
# print ('''
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⠹⡆⢀⣤⣤⡀⢠⣤⢠⣤⣿⡤⣴⡆⠀⣴⠀⠀⠀⢠⣄⠀⢠⡄⠀⠀⠀⣤⣄⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠰⠆⠀⣷⢸⣧⣀⡀⢸⢹⡆⠀⢸⡇⠠⣧⢤⣿⠀⠀⠀⢸⡟⣦⣸⡇⡞⡙⢣⡀⢠⡇⠀⢿⠋⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⣠⠟⢸⣇⣀⡀⣿⠉⢻⡀⢸⡇⠀⣿⠀⣿⠀⠀⠀⣸⡇⠘⢿⡏⢇⣁⡼⠃⣼⠃⠀⣼⡓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#          ⠀⠀⠀⡿⠒⠋⠁⠀⠈⠉⠉⠁⠉⠀⠀⠀⠀⠉⠀⠉⠀⠉⠀⠀⠀⠉⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠛⠓⠲⠂⠀⠀''')

# if Person == "si":
#     Cafe = True
#     print ("Ryuk: Ya esta tomada la decisión")
#     time.sleep(2)
#     print ("La persona que te estaba viendo era una chica por que te veia atractivo pero ahora por ponerle") 
#     print (" su nombre en el cuaderno el café que tomaba le hizo hervir los organos hasta explotar y perdiste la oportunidad de ponerla")
# elif Person == "no":
#     Cafe = False 
#     print ("Ryuk: Pense que fueras mas interesante")
#     print ("Ryuk se va a llorar por su cuchurrumin (Kira)")
# else:
#     print ("Ponen tu nombre en la death note por no responder bien y pal lobby")

# EJERCICIO 3

# Menu=0

# while Menu!=4:
#     print('''
#           1. Comprar
#           2. Pagar
#           3. Descuento
#           4. Salir''')
#     Menu=int(input("Ingrese una opcion: "))
#     if Menu==1:
#         print ('''Las siguientes opciones son: 
#                1. Leche 
#                2. Marvel Legends 
#                3. Ugancio''')
        
#     elif Menu==2:
#         print ('''
#                Lo siguiente que comprara es: 
#                ''')
    
#     elif Menu==3:
#         print ('''
#               Tenga su descuento de 30%''')
        
#     elif Menu==4:
#         print ("Saliendo...")

#     else:
#         print ("Escribe bien mrd")

#EJERCICIO 4

# Biblio=0
# import time

# while Biblio!=4:
#     print (''' 
#        BIENVENIDO A NUESTRA BIBLIOTECA MINI UGANCIO
#        Que es lo que desea llevar en nuestra seccion''')
#     time.sleep(2)
#     print ('''
#        1. Uzumaki
#        2. Berserk
#        3. Fullmetal Alchemist
#        4. Salir''')
#     Biblio=int(input("Ingrese su Manga deseado: "))

#     if Biblio==1:
#             print ("Agregando al carrito Uzumaki...")

#     elif Biblio==2:
#             print ("Agregando al carrito Berserk...")

#     elif Biblio==3:
#             print ("Agregando al carrito Fullmetal Alchemist...")

#     elif Biblio==4:
#             print ("Saliendo del sistema...")
        
#     else:
#             print ("Escriba bien mamabicho")





# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un
# cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario
# decida que su pedido está completo.

Pikachu = 4500
Pikachu_c = 0
Otaku = 5000
Otaku_c = 0
Pulpo = 5200
Pulpo_c = 0
Anguila = 4800
Anguila_c = 0
total = 0
descuento = 0
rollitos = 0


while True:
        print ("BIENVENIDO A NUESTRO DELIVERY DE SUSHI")
        print ('''Te ofrecemos las siguientes opciones:
                1. Pikachu Roll $4500
                2. Otaku Roll $5000
                3. Pulpo Venenoso Roll $5200
                4. Anguila Eléctrica Roll $4800
                5. Ver Boleta
                6. Completar Pedido con descuento
                7. Salir
        ''')
        op = int(input("Elija una opción: "))

        if op == 1:
                total = total + Pikachu
                rollitos = rollitos + 1
                Pikachu_c = Pikachu_c + 1
                print (f"Su Pikachu Roll ya esta agregado!!! Por lo tanto lleva {rollitos} y su valor de ahora es: {total}")
        
        elif op == 2:
                total = total + Otaku
                rollitos = rollitos + 1
                Otaku_c = Otaku_c + 1
                print (f"Su Otaku Roll ya esta agregado!!! Por lo tanto lleva {rollitos} y su valor de ahora es: {total}")
        
        elif op == 3:
                total = total + Pulpo
                rollitos = rollitos + 1
                Pulpo_c = Pulpo_c + 1
                print (f"Su Pulpo Venoso Roll ya esta agregado!!! Por lo tanto lleva {rollitos} y su valor de ahora es: {total}")
        
        elif op == 4:
                total = total + Anguila
                rollitos = rollitos + 1
                Anguila_c = Anguila_c + 1
                print (f"Su Anguila Eléctrica Roll ya esta agregado!!! Por lo tanto lleva {rollitos} y su valor de ahora es: {total}")

        elif op == 5:
                print ("Ahora vera su boleta segun lo elegido a su gusto: ")
                print (f''' 
                Rollos que lleva: {rollitos}
                  Pikachu Roll = {Pikachu_c}
                  Otaku Roll = {Otaku_c}
                  Pulpo Venenoso Roll = {Pulpo_c}
                  Anguila Eléctrica Roll = {Anguila_c}
                Precio total = {total}
                ''')
        
        while op == 6:
                desc=str(input("Ingrese codigo de descuento: "))
                if desc == "soyotaku":
                        total = total * 0.90
                        print (f"Su codigo se aplico correctamente, ahora con su descuento su codigo es: {total}")
                else:
                        print ("código no válido")
                        desc = int(input("Desea volver a intentarlo?"))
                        print (''' 
                        1. Si
                        2. No ''')
                        if desc == 1:
                                op == 5
                        else: 
                                break
                        