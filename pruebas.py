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
        
        elif op == 7:
                print ("Saliendo del sistema...")
                break
        while op == 6:
                desc=str(input("Ingrese codigo de descuento: "))
                if desc == "soyotaku":
                        total = total * 0.90
                        print (f"Su codigo se aplico correctamente, ahora con su descuento su codigo es: {total}")
                else:
                        print ("código no válido")
                        desc = str(input('''Desea volver a intentarlo?
                        1. Si
                        2. No 
                        '''))

                        if desc == "Si":
                                op == 6
                        elif desc == "No":
                            print ("Entoncecs volvera al MENU PRINCIPAL...")
                            break