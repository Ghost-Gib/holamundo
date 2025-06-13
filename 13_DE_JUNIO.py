productos=["Monitor", "Mouse", "Teclado"]
precios=[120000, 22000, 45000]
carrito=[]
while True:
    while True:
        try:
            print(''' 
            1.- Agregar Productos 
            2.- Comprar
            3.- Crear Boleta
            4.- Salir''')
            op=int(input("Seleccione una opcion: "))
            break
        except Exception:
            print ("Opcion no valida")
    match op:
        case 1:
            prod=input("Ingrese un producto: ")
            productos.append(prod)
            pre=int(input("Ingrese el precio: "))
            precios.append(pre)
        case 2:
            for i in range(len(productos)):
                print(i+1, productos[i], "$", precios[i])
            producto=int(input("Seleccione una opcion: "))
            carrito.append(producto)
            print(carrito)
        case 3:
            total = 0
            print ("-----------BOLETA-----------")
            print ("Productos de computacion:")
            for i in range (len(carrito)):
                print (f"{productos[i]} $ {precios[i]}")
                total=total+precios[i]
            print ("Los productos que lleva en total serian", producto-1)
            print ("Precio total neto =", total)
            print ("Precio total + IVA =", total*1.19)

                # print (f"Precio total neto = {total} \n Precio total + IVA = {total*1.19}")