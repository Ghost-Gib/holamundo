#primero programar un menu funcional para ir agregando rolls al pedido, 


print("Bienvenido a sushimbombo")
pikachu = 4500
pika_c = 0
otaku = 5000
otaku_c = 0
venoso= 5200
venoso_c = 0
anguila = 4800
anguila_c=0
total = 0
descuento = False
rolls = 0

while True:
    print("""Que desea agregar?
          nuestras opciones son:
          1) PIKACHU ROLL: 4500 $
          2) OTAKU ROLL 5000 $
          3) PULPO VENOSO ROLL $
          4) ANGUILA ELECTRICA ROLL $
          5) CODIGO DE DESCUENTO
          7) VER BOLETA
          6) SALIR
          """)
    opc = int(input("Ingrese su opcion: ").strip())
    if opc == 1:
        total = total + pikachu
        rolls = rolls + 1
        pika_c = pika_c+1
        print (f"Ha agregado un pikachu roll, su total asciende a {total} y lleva {rolls} rolls")
    elif opc == 2:
        total = total + otaku
        rolls = rolls +1
        otaku_c = otaku_c +1
        print(f"Ha agregado un OTAKU ROLL a su pedudo, su total asciende a {total}y lleva {rolls} rolls")
    elif opc == 3:
        total = total + venoso
        rolls = rolls +1
        venoso_c = venoso_c+1
        print(f"Ha agregado un pulpo venoso roll, su total asciende a {total} y lleva {rolls} rolls")
    elif opc == 4:
        total = total + anguila
        anguila_c=anguila_c+1
        rolls = rolls +1
        print(f"Ha agregado un Anguila electrica roll, su total asciende a {total} y lleva {rolls} rolls")
    elif opc == 7:
        print(f"""
            Lleva un total de {rolls} rolls
            Pikachu rolls : {pika_c}
            Otaku rolls : {otaku_c}
            Pulpo venoso rolls : {venoso_c}
            Anguila electrica roll : {anguila_c}
            Su total a pagar es de {total}
                """
              )
    elif opc == 6:
        print("vuelva pronto! ")
        break
    else:
        print("Ingrese un solo caracteres numericos por favor")
    while opc == 5:
        dcto = str(input("Ingrese su codigo de descuento: ")).strip()
        if dcto == "soyotaku":
            total = total * 0.90
            print(f"codigo ingresado correctamente, su total baja a {total}")
        else:
            dcto = int(input("codigo invalido\ndesea volver a intentarlo? \n1) si \n2) no\n"))
            if dcto == 1:
                opc == 5
            else:
                break