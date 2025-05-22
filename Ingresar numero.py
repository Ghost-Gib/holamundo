import time
while True:
    try: 
        op=int(input("Ingrese un número: "))
        break 
    except Exception:
        time.sleep(2)
        print("Solo se permiten números")
        time.sleep(3)
        print("Las flores cantan")
        time.sleep(2)
        print("Eran las aves pero ahora si")
        time.sleep(3)
        print("Intente nuevamente")