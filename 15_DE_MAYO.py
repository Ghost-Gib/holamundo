# uso y explicación de match

def suma():
   n1=int(input("Ingrese un numero: "))
   n2=int(input("Ingrese otro numero: "))
   print("El resultado de la suma es", n1+n2)

def resta():
   n1=int(input("Ingrese un numero: "))
   n2=int(input("Ingrese otro numero: "))
   print("El resultado de la resta es", n1-n2)

def multiplicación():
   n1=int(input("Ingrese un numero: "))
   n2=int(input("Ingrese otro numero: "))
   print("El resultado de la multiplicación es", n1*n2)

def división():
   try:
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("El resultado de la división es", n1/n2)
   except ZeroDivisionError as renapro:
    print(f"Se produjo una excepción: {renapro}")

def potencia():
   base = int(input("Ingrese la base: "))
   exponente = int(input("Ingrese el exponente: "))
   print("El resultado de la potencia es", base**exponente)


while True:
    print('''
      1. Suma
      2. Resta
      3. Multiplicar
      4. Dividir
      5. Potencia
      6. Salir
      ''') 
    op=int(input("Seleccione una opción: "))

    match op:
     case 1:
        print("Suma")
        suma()

     case 2:
         print("Resta")
         resta ()

     case 3:
        print("Multiplicar")
        multiplicación()
    
     case 4:
        print("Dividir")
        división()

     case 5:
        print("Potencia")
        potencia()
    
     case 6:
        print("Bye bye")
        break
     case _:
      print("Opción no valida")