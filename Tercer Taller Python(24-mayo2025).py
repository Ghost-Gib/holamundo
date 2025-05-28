# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except Exception:
#         print ("Solo puedes ingresar numeros")

try:
    num=int (input("Ingrese un numero: "))
except Exception:
    print("Solo puedes ingresar numeros")
else:
    print ("Si no hay excepciones")
finally:
    print("Esto se ejecuta siempre, haya o no excepciones")