import time

Amor = str(input("Miren quien es, es la guapa de mi novia jiji (Apreta la tecla Enter): "))
print("----------------------Mi amorcito que es lo que desea???----------------------")

while True:
    while True:
        print('''
              Selecciona la opción que quieras baby <3 :
              1. Besitos
              2. Un chiste
              3. Un recuerdo
              4. Salir
              ''')
        op = int(input())
        break

    match op:
        case 1:
            while True:
                    print ("Otiaaa entonces te ganaste muchos besitos baby jiji")
                    time.sleep (0.6)
                    print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⣶⣼⣷⣷⣤⣄⢀⣄⠀⠀⠀⠀⢀⣶⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⣀⣰⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣷⣶⡆⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡿⣿⣿⣿⣾⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣿⣿⣷⣻⢳⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⢿⣿⣯⣻⣿⣾⣿⣯⣿⣹⡿⣿⡏⣿⡿⣿⡇⣿⣿⣿⠁⣿⣿⢰⣿⣽⣿⣿⢻⣿⡟⣾⣿⣯⣿⣿⣿⣿⣿⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⣰⣿⣿⣿⣿⣿⣿⡻⣿⣷⣿⣞⣿⣿⣿⣻⣿⢻⡇⣿⣿⠘⣿⣿⣿⡟⣿⣿⣧⢿⡇⣿⣿⣿⠇⣿⣿⣟⢠⣿⣃⣼⠇⣹⣿⣵⣿⡿⢡⣿⣿⡟⣵⣿⣿⣿⡽⣿⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢹⣿⣿⣿⣿⣿⣿⣷⣿⣷⣹⣿⡿⣿⣽⣿⡜⣿⣿⡼⣿⣼⣿⠀⠉⢁⠀⠃⣿⣿⣿⢸⡇⢸⣿⣿⣨⣿⢻⡏⢹⣿⣿⠏⠠⣿⣿⣿⣿⡧⠿⢛⠉⣴⣿⠟⢡⡿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣩⣽⣿⣿⣿⡿⣿⣾⡛⣿⣷⣿⣷⢻⣿⣿⣿⡞⣿⣷⢻⣧⣿⣃⣠⣼⣇⢀⣿⣿⣿⣿⣿⠀⠿⠻⣿⠃⢸⠃⣼⣿⠏⠀⣰⣿⣿⣿⢋⣴⣾⣿⣿⠿⢋⣴⣏⡀⠙⠛⣱⠆
⠀⠀⠀⠀⠀⠀⣂⣾⣵⣿⣿⣿⣿⡽⣷⡽⣿⣷⡼⣿⣿⣿⣧⡿⣿⣿⣿⡞⣿⡏⣿⠟⠉⠀⢻⡉⠘⠉⠃⣽⢻⡇⠀⣴⣶⣷⣴⠇⢠⣿⣿⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⠟⣶⡿⠀
⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣯⡻⣿⣎⢿⣼⢿⣇⠹⣿⣿⣿⣿⡿⢿⣿⣷⠈⣿⡌⣦⣶⣴⣼⣷⣖⣮⣿⣿⣹⣷⣾⣿⢿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠁⠀
⠀⠀⠀⠀⣬⣿⣿⣿⣿⢿⣿⣝⣿⣾⣿⣾⠿⣆⣻⣆⠈⠻⣯⣽⡿⢿⡻⣿⣄⡟⢿⢫⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠿⣿⠟⢛⡻⣿⣿⣿⣿⠿⠷⠖⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⢿⣭⠻⣝⢿⣷⣽⣤⣙⠿⢿⣷⣤⡘⠳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣀⣹⣽⣿⣿⣿⣿⣿⣷⣿⣿⣾⣦⣬⡿⠇⠀⠀⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⡿⣿⣿⣧⣈⠙⠿⣿⣿⣿⣿⣾⣿⣿⣿⣷⣮⣙⣿⣿⣿⣿⣿⠏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣿⣿⣿⣿⣿⢿⣿⣻⣻⣹⡯⠳⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⣺⣿⣿⣿⣿⣿⢿⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠿⠿⠟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢾⣿⣿⢿⣿⣏⠘⣿⣿⣼⢧⣻⣏⣏⣷⠀⢨⠀⠠⣄⢀⣆⡀⠀⠀
⣐⣿⣿⠿⣛⣿⣿⣷⣾⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⢀⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⢟⣙⠻⣿⣿⡿⠙⣷⣿⣄⣿⣿⣷⡘⢿⣿⣷⡘⣧⣶⣿⡄⢻⣿⠀⠀
⠈⣿⣯⣤⣹⡿⢿⣿⣿⣿⣿⣿⣿⣿⠿⣫⣿⣿⣿⣇⣴⣾⣿⣿⡟⠉⠉⠉⠙⢻⡶⣤⣾⣷⣤⣶⣤⣄⣤⣀⠀⢰⣿⢿⣿⣿⣿⣆⣹⣿⣿⣎⢹⣿⣿⣿⣿⣿⣷⡈⢿⣿⣷⡼⣿⣿⣿⡌⢿⣤⡀
⠀⠈⠳⢢⣿⣿⣶⣾⣿⡿⢿⣿⣿⣷⣿⣿⣿⣿⣿⠟⠛⢘⢁⣎⢠⠴⠀⣴⣾⠏⣼⣙⣻⠉⣡⡰⣍⣿⣿⣾⢷⠘⣻⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣼⣿⣿⣿⠶⠁⠀
⠀⠀⠈⠺⣭⣿⠿⠋⠀⠀⣼⡿⣿⣟⡟⠻⢷⣮⡷⢳⡄⢻⠚⠁⠁⣀⣠⣼⡃⠀⣌⣼⣹⠂⠘⣧⣧⢰⣤⣿⠀⠀⣯⣿⣿⣿⣇⣽⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡸⣿⣿⣿⣿⠿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡟⢿⠻⡯⢹⣯⡇⢠⣌⢯⣤⣶⢰⣿⣏⠺⣇⠀⣯⣿⢿⠦⣼⣯⣿⡇⣾⠟⣷⣦⠼⣿⣷⢹⣿⣷⣿⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢽⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢸⣿⣷⢸⣿⣿⣸⣿⡄⣴⣿⣾⣿⣿⣷⣿⣿⣿⣹⣠⣿⣿⣼⣆⢸⣿⣿⣟⢸⣯⣽⣿⡄⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡈⢿⣿⠜⣿⣿⣿⣿⡆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⡞⣿⣿⣿⣷⢸⣿⣿⡜⣿⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣦⣽⣷⣸⣶⣆⢻⣿⣿⣿⣿⢸⣿⣿⢋⣿⣿⡿⣿⣿⣿⢾⣿⣿⣿⣿⢼⣿⣿⣿⡇⢿⣿⣿⣿⣾⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⢻⣿⣿⣿⣿⣬⣿⣿⣿⣿⡸⣿⣿⣮⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⡎⣿⣿⣿⣯⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢺⣿⡿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⢿⣿⡿⣿⣿⢿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠻⢿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠻⠿⠏⢿⣿⢿⣿⣿⣯⣿⣿⣿⣿⣾⣿⣿⣿⣿⡿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠸⠿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                    time.sleep (0.6)
                    print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣯⣿⣝⡻⢏⡯⣛⡟⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⢻⡝⣦⣷⣾⣓⣮⡲⡵⣎⣗⡺⢏⣖⣛⠳⣿⣵⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣷⣿⣿⡾⣿⣶⣦⣤⣠⢿⣿⣿⣞⡯⣿⣯⣿⣷⡿⣼⣷⢿⡲⣟⡿⣯⢯⡇⡝⣦⠼⢟⡿⢻⣿⣷⢶⢦⡄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⢿⣤⣻⣿⣻⣿⡻⣿⣟⣧⣿⣟⣧⣧⣿⣻⣟⣻⣃⣿⢟⣿⣻⣸⣿⢿⣧⡟⢿⣻⢜⣧⢛⣤⠿⣛⡟⣿⣼⢟⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡟⣭⢿⡾⣿⣿⣿⣿⣿⣿⢿⣷⣯⣵⣿⣿⣽⣻⢿⡳⣿⣞⢿⣽⡏⣼⡾⣿⣿⣯⣿⣿⡿⣿⣹⣿⣽⣿⣷⣻⣭⡻⢜⡞⣮⢿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣻⢭⢿⡽⣯⣟⣻⣿⣿⣿⣿⣿⣿⣿⣯⣽⣿⣿⣷⢯⣿⡷⣏⣿⠿⡧⣿⢯⣿⢿⣷⣿⣟⣶⣿⣿⣯⣽⣿⣟⣟⣿⣼⡗⡯⢟⣶⣻⣟⣻⡆⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣯⣷⣿⣿⣯⣿⡽⣟⣿⣿⣿⣿⣿⣿⣿⣟⣷⣷⣿⣽⣿⢿⣟⣿⣟⣿⣿⣝⠘⣷⡾⣿⡿⣻⣯⣿⣿⡿⣷⢺⣯⣿⣯⣿⢾⣿⡽⣯⣳⢾⢾⣽⡇⠀
⠀⠀⠀⠀⢀⣼⢿⣳⣮⣛⣼⣿⣿⡿⣿⢿⡻⣼⣿⢟⣿⣟⣿⢿⣿⣿⡯⣷⢻⣿⡿⣿⣽⠿⣿⡞⢠⣿⣿⢿⢻⣷⠿⣟⠷⣻⢿⣫⡧⢏⡟⣣⣞⣳⡷⣶⡼⣻⣽⣏⠀⠀
⠀⠀⠀⢠⣾⣟⣿⣿⢻⡻⣝⣺⣿⢿⣿⣿⣯⢿⣽⣿⡿⣿⣿⣿⣿⣾⣿⣿⣻⣼⢿⣯⣿⣿⢾⣵⠰⢾⡋⣿⣳⣿⣿⡿⣿⢿⣿⡿⠿⠿⠿⠟⠻⠯⠛⣿⣻⣿⣿⠃⠀⠀
⠀⠀⢀⣶⣿⣻⢮⡝⣷⣹⢿⣴⣻⣯⣿⣾⡟⣿⣿⣿⣿⢿⣿⢿⣟⣷⣯⣷⣿⣯⣿⡾⣿⣿⢻⡟⠈⢱⣿⠟⠋⠿⠁⠀⠀⠀⠁⣀⣤⣤⡤⣤⣤⣤⣤⣌⣿⣫⣥⣠⡀⠀
⠀⠀⣟⣿⡒⢯⢳⣽⣷⢿⣯⢿⠿⣿⣛⣿⣿⣻⢾⣷⣿⣿⡾⣿⣿⣯⣿⣿⣿⣽⣯⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⣀⡤⣴⣶⣿⣿⣿⢟⢧⣉⣧⢯⣳⣽⢿⢻⣽⣻⣿⣿⡀
⠀⣰⡟⢫⠖⣥⣻⢯⣾⣿⣟⣿⣹⣷⣿⢷⣟⣮⡙⡶⡛⣿⢮⠻⡿⠟⡿⡻⠋⠃⠛⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣟⣭⣷⣝⡾⣿⣽⢛⣯⣿⣣⢟⣮⣿⣻⣽⣻⣿⠃
⡠⣱⠞⣡⡛⢮⣝⡻⣿⠾⡿⠛⢉⣟⣹⣬⣾⢶⣽⣯⣶⡷⣶⡖⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣹⡾⣿⣷⢿⡽⣿⣞⡿⣷⣳⣿⢿⣟⣮⣷⢳⣞⣻⠈⠀
⣜⠇⣱⢬⢯⢷⣬⢟⢫⣩⣴⣞⣿⣾⢯⠟⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⡟⣿⣽⣿⡿⣿⣿⣯⡵⣫⡿⣿⣻⣿⢿⢯⢿⢫⣝⣷⣿⡝⠀⠀
⠡⣴⡪⣧⢮⠯⢍⣞⡯⣷⡞⣹⠟⠉⢀⣀⣠⢄⣴⣶⣲⣦⣤⣄⣀⣠⣀⣤⣤⣴⣦⣴⣾⣿⣿⣿⣿⣻⣽⣾⣿⣾⣻⡟⣏⣿⣿⣽⣿⣟⣽⣿⢯⣳⣾⢯⣟⣾⠏⠀⠀⠀
⣠⣷⡳⢿⢬⡾⢯⣿⣻⣿⣿⣧⣲⠿⡿⡳⡻⢿⢻⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣾⢯⣿⣟⡾⣹⡶⣯⣷⣻⡽⣿⣽⣿⣷⣿⣯⣳⡿⣗⣿⠎⠀⠀⠀⠀
⣛⡷⣧⣝⣻⣽⣿⣿⡿⣻⠋⠁⠀⡠⣔⠢⣉⣾⣯⡯⣗⣿⣞⣯⣿⣻⣽⣿⣿⣿⣯⣟⣷⣻⣷⣻⣿⣟⣿⣯⣻⣽⣷⣿⣻⡷⣟⡟⣿⣿⣿⣷⣿⡵⡗⢧⠁⠀⠀⠀⠀⠀
⠉⠁⠉⠩⣿⡽⠓⣧⢣⣁⢱⢦⣱⣏⣿⡸⣿⣺⣷⣟⣯⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡯⣿⣟⣿⣿⡽⣾⣏⢷⣽⣧⣯⣟⣾⡿⣿⣛⣷⣛⣿⠛⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⣵⣲⣷⢻⣥⡟⣿⡿⣾⣿⣟⣷⣿⣻⣷⣿⣿⣟⣿⣿⣟⣿⣟⣿⢿⣿⣯⣿⣾⡷⣿⣻⣟⣷⣿⣿⣽⣾⢏⣷⣷⣮⣷⣻⢷⣻⣞⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣯⣿⣿⣬⡏⢻⣿⣧⣿⣷⡟⣯⣿⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣽⣷⣿⣿⣯⣿⣿⣷⣯⣿⣾⣿⣽⣷⢻⣽⣾⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⢝⣞⡿⣏⡽⣪⡵⢿⣻⣽⣟⣿⡿⣟⡿⣷⣻⣽⢿⣼⣷⣻⣟⣿⣽⣾⣾⣿⣿⣿⢿⣞⣿⣻⣿⣿⣿⣿⣻⣯⣿⣿⣟⡻⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠓⠂⠧⣯⢏⡧⣿⢻⣏⣿⣿⢿⣯⣟⣾⣻⢿⣳⣯⣷⡿⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠛⠿⠜⣯⣞⣻⣾⣻⣾⣽⣿⣽⣻⡿⣟⣿⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠘⠙⠛⠓⠿⣿⡿⠿⠟⢿⣾⣿⣿⠿⠿⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                    time.sleep (0.6)
                    
                    print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣽⣯⣿⣿⣞⣦⣄⣤⣀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⢻⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣀⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣼⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣐⣿⣿⣾⣿⡿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣜⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⣵⣥⣦⠀⠀⠀
            ⠀⠀⠈⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣻⢻⢟⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠯⠖⠁⠀⠀
            ⠀⠀⢰⣿⣻⣿⣿⣿⣿⣿⣿⡿⣿⠿⡿⠿⠚⠊⠁⠀⠀⠀⠀⠀⠈⠉⠙⠟⢿⢿⠟⠋⠀⣤⣤⡄⠀⠀
            ⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣿⣿⣿⢿⡿⣶⣶⣿⣏⣆⠀⠀⠀
            ⠀⢀⣷⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⠂⠀⠀⠀
            ⠀⢘⣿⣿⣿⣿⣿⣿⡿⢋⣁⣄⣀⡀⠀⠀⠀⠀⣀⣶⣿⣿⣻⣿⣿⣻⣿⣿⣿⣿⣿⣿⢟⠏⠀⠀⠀⠀
            ⢠⣻⣿⣿⣿⣿⢿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣻⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀
            ⠾⠟⠛⠉⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡿⠁⠀⠀⠀⠀⠀⠀
            ⠒⢲⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠸⠿⣼⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣾⣿⣿⠿⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢓⠛⠿⠿⠿⣿⠿⠿⣿⢿⠿⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                    
                    time.sleep (0.6)
                    print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⣶⣼⣷⣷⣤⣄⢀⣄⠀⠀⠀⠀⢀⣶⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⣀⣰⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣷⣶⡆⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡿⣿⣿⣿⣾⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣿⣿⣷⣻⢳⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⢿⣿⣯⣻⣿⣾⣿⣯⣿⣹⡿⣿⡏⣿⡿⣿⡇⣿⣿⣿⠁⣿⣿⢰⣿⣽⣿⣿⢻⣿⡟⣾⣿⣯⣿⣿⣿⣿⣿⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⣰⣿⣿⣿⣿⣿⣿⡻⣿⣷⣿⣞⣿⣿⣿⣻⣿⢻⡇⣿⣿⠘⣿⣿⣿⡟⣿⣿⣧⢿⡇⣿⣿⣿⠇⣿⣿⣟⢠⣿⣃⣼⠇⣹⣿⣵⣿⡿⢡⣿⣿⡟⣵⣿⣿⣿⡽⣿⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢹⣿⣿⣿⣿⣿⣿⣷⣿⣷⣹⣿⡿⣿⣽⣿⡜⣿⣿⡼⣿⣼⣿⠀⠉⢁⠀⠃⣿⣿⣿⢸⡇⢸⣿⣿⣨⣿⢻⡏⢹⣿⣿⠏⠠⣿⣿⣿⣿⡧⠿⢛⠉⣴⣿⠟⢡⡿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣩⣽⣿⣿⣿⡿⣿⣾⡛⣿⣷⣿⣷⢻⣿⣿⣿⡞⣿⣷⢻⣧⣿⣃⣠⣼⣇⢀⣿⣿⣿⣿⣿⠀⠿⠻⣿⠃⢸⠃⣼⣿⠏⠀⣰⣿⣿⣿⢋⣴⣾⣿⣿⠿⢋⣴⣏⡀⠙⠛⣱⠆
⠀⠀⠀⠀⠀⠀⣂⣾⣵⣿⣿⣿⣿⡽⣷⡽⣿⣷⡼⣿⣿⣿⣧⡿⣿⣿⣿⡞⣿⡏⣿⠟⠉⠀⢻⡉⠘⠉⠃⣽⢻⡇⠀⣴⣶⣷⣴⠇⢠⣿⣿⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⠟⣶⡿⠀
⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣯⡻⣿⣎⢿⣼⢿⣇⠹⣿⣿⣿⣿⡿⢿⣿⣷⠈⣿⡌⣦⣶⣴⣼⣷⣖⣮⣿⣿⣹⣷⣾⣿⢿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠁⠀
⠀⠀⠀⠀⣬⣿⣿⣿⣿⢿⣿⣝⣿⣾⣿⣾⠿⣆⣻⣆⠈⠻⣯⣽⡿⢿⡻⣿⣄⡟⢿⢫⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠿⣿⠟⢛⡻⣿⣿⣿⣿⠿⠷⠖⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⢿⣭⠻⣝⢿⣷⣽⣤⣙⠿⢿⣷⣤⡘⠳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣀⣹⣽⣿⣿⣿⣿⣿⣷⣿⣿⣾⣦⣬⡿⠇⠀⠀⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⡿⣿⣿⣧⣈⠙⠿⣿⣿⣿⣿⣾⣿⣿⣿⣷⣮⣙⣿⣿⣿⣿⣿⠏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣿⣿⣿⣿⣿⢿⣿⣻⣻⣹⡯⠳⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⣺⣿⣿⣿⣿⣿⢿⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠿⠿⠟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢾⣿⣿⢿⣿⣏⠘⣿⣿⣼⢧⣻⣏⣏⣷⠀⢨⠀⠠⣄⢀⣆⡀⠀⠀
⣐⣿⣿⠿⣛⣿⣿⣷⣾⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⢀⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⢟⣙⠻⣿⣿⡿⠙⣷⣿⣄⣿⣿⣷⡘⢿⣿⣷⡘⣧⣶⣿⡄⢻⣿⠀⠀
⠈⣿⣯⣤⣹⡿⢿⣿⣿⣿⣿⣿⣿⣿⠿⣫⣿⣿⣿⣇⣴⣾⣿⣿⡟⠉⠉⠉⠙⢻⡶⣤⣾⣷⣤⣶⣤⣄⣤⣀⠀⢰⣿⢿⣿⣿⣿⣆⣹⣿⣿⣎⢹⣿⣿⣿⣿⣿⣷⡈⢿⣿⣷⡼⣿⣿⣿⡌⢿⣤⡀
⠀⠈⠳⢢⣿⣿⣶⣾⣿⡿⢿⣿⣿⣷⣿⣿⣿⣿⣿⠟⠛⢘⢁⣎⢠⠴⠀⣴⣾⠏⣼⣙⣻⠉⣡⡰⣍⣿⣿⣾⢷⠘⣻⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣼⣿⣿⣿⠶⠁⠀
⠀⠀⠈⠺⣭⣿⠿⠋⠀⠀⣼⡿⣿⣟⡟⠻⢷⣮⡷⢳⡄⢻⠚⠁⠁⣀⣠⣼⡃⠀⣌⣼⣹⠂⠘⣧⣧⢰⣤⣿⠀⠀⣯⣿⣿⣿⣇⣽⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡸⣿⣿⣿⣿⠿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡟⢿⠻⡯⢹⣯⡇⢠⣌⢯⣤⣶⢰⣿⣏⠺⣇⠀⣯⣿⢿⠦⣼⣯⣿⡇⣾⠟⣷⣦⠼⣿⣷⢹⣿⣷⣿⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢽⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢸⣿⣷⢸⣿⣿⣸⣿⡄⣴⣿⣾⣿⣿⣷⣿⣿⣿⣹⣠⣿⣿⣼⣆⢸⣿⣿⣟⢸⣯⣽⣿⡄⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡈⢿⣿⠜⣿⣿⣿⣿⡆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⡞⣿⣿⣿⣷⢸⣿⣿⡜⣿⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣦⣽⣷⣸⣶⣆⢻⣿⣿⣿⣿⢸⣿⣿⢋⣿⣿⡿⣿⣿⣿⢾⣿⣿⣿⣿⢼⣿⣿⣿⡇⢿⣿⣿⣿⣾⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⢻⣿⣿⣿⣿⣬⣿⣿⣿⣿⡸⣿⣿⣮⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⡎⣿⣿⣿⣯⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢺⣿⡿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⢿⣿⡿⣿⣿⢿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠻⢿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠻⠿⠏⢿⣿⢿⣿⣿⣯⣿⣿⣿⣿⣾⣿⣿⣿⣿⡿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠸⠿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                    time.sleep (0.6)
                    print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣯⣿⣝⡻⢏⡯⣛⡟⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⢻⡝⣦⣷⣾⣓⣮⡲⡵⣎⣗⡺⢏⣖⣛⠳⣿⣵⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣷⣿⣿⡾⣿⣶⣦⣤⣠⢿⣿⣿⣞⡯⣿⣯⣿⣷⡿⣼⣷⢿⡲⣟⡿⣯⢯⡇⡝⣦⠼⢟⡿⢻⣿⣷⢶⢦⡄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⢿⣤⣻⣿⣻⣿⡻⣿⣟⣧⣿⣟⣧⣧⣿⣻⣟⣻⣃⣿⢟⣿⣻⣸⣿⢿⣧⡟⢿⣻⢜⣧⢛⣤⠿⣛⡟⣿⣼⢟⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡟⣭⢿⡾⣿⣿⣿⣿⣿⣿⢿⣷⣯⣵⣿⣿⣽⣻⢿⡳⣿⣞⢿⣽⡏⣼⡾⣿⣿⣯⣿⣿⡿⣿⣹⣿⣽⣿⣷⣻⣭⡻⢜⡞⣮⢿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣻⢭⢿⡽⣯⣟⣻⣿⣿⣿⣿⣿⣿⣿⣯⣽⣿⣿⣷⢯⣿⡷⣏⣿⠿⡧⣿⢯⣿⢿⣷⣿⣟⣶⣿⣿⣯⣽⣿⣟⣟⣿⣼⡗⡯⢟⣶⣻⣟⣻⡆⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣯⣷⣿⣿⣯⣿⡽⣟⣿⣿⣿⣿⣿⣿⣿⣟⣷⣷⣿⣽⣿⢿⣟⣿⣟⣿⣿⣝⠘⣷⡾⣿⡿⣻⣯⣿⣿⡿⣷⢺⣯⣿⣯⣿⢾⣿⡽⣯⣳⢾⢾⣽⡇⠀
⠀⠀⠀⠀⢀⣼⢿⣳⣮⣛⣼⣿⣿⡿⣿⢿⡻⣼⣿⢟⣿⣟⣿⢿⣿⣿⡯⣷⢻⣿⡿⣿⣽⠿⣿⡞⢠⣿⣿⢿⢻⣷⠿⣟⠷⣻⢿⣫⡧⢏⡟⣣⣞⣳⡷⣶⡼⣻⣽⣏⠀⠀
⠀⠀⠀⢠⣾⣟⣿⣿⢻⡻⣝⣺⣿⢿⣿⣿⣯⢿⣽⣿⡿⣿⣿⣿⣿⣾⣿⣿⣻⣼⢿⣯⣿⣿⢾⣵⠰⢾⡋⣿⣳⣿⣿⡿⣿⢿⣿⡿⠿⠿⠿⠟⠻⠯⠛⣿⣻⣿⣿⠃⠀⠀
⠀⠀⢀⣶⣿⣻⢮⡝⣷⣹⢿⣴⣻⣯⣿⣾⡟⣿⣿⣿⣿⢿⣿⢿⣟⣷⣯⣷⣿⣯⣿⡾⣿⣿⢻⡟⠈⢱⣿⠟⠋⠿⠁⠀⠀⠀⠁⣀⣤⣤⡤⣤⣤⣤⣤⣌⣿⣫⣥⣠⡀⠀
⠀⠀⣟⣿⡒⢯⢳⣽⣷⢿⣯⢿⠿⣿⣛⣿⣿⣻⢾⣷⣿⣿⡾⣿⣿⣯⣿⣿⣿⣽⣯⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⣀⡤⣴⣶⣿⣿⣿⢟⢧⣉⣧⢯⣳⣽⢿⢻⣽⣻⣿⣿⡀
⠀⣰⡟⢫⠖⣥⣻⢯⣾⣿⣟⣿⣹⣷⣿⢷⣟⣮⡙⡶⡛⣿⢮⠻⡿⠟⡿⡻⠋⠃⠛⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣟⣭⣷⣝⡾⣿⣽⢛⣯⣿⣣⢟⣮⣿⣻⣽⣻⣿⠃
⡠⣱⠞⣡⡛⢮⣝⡻⣿⠾⡿⠛⢉⣟⣹⣬⣾⢶⣽⣯⣶⡷⣶⡖⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣹⡾⣿⣷⢿⡽⣿⣞⡿⣷⣳⣿⢿⣟⣮⣷⢳⣞⣻⠈⠀
⣜⠇⣱⢬⢯⢷⣬⢟⢫⣩⣴⣞⣿⣾⢯⠟⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⡟⣿⣽⣿⡿⣿⣿⣯⡵⣫⡿⣿⣻⣿⢿⢯⢿⢫⣝⣷⣿⡝⠀⠀
⠡⣴⡪⣧⢮⠯⢍⣞⡯⣷⡞⣹⠟⠉⢀⣀⣠⢄⣴⣶⣲⣦⣤⣄⣀⣠⣀⣤⣤⣴⣦⣴⣾⣿⣿⣿⣿⣻⣽⣾⣿⣾⣻⡟⣏⣿⣿⣽⣿⣟⣽⣿⢯⣳⣾⢯⣟⣾⠏⠀⠀⠀
⣠⣷⡳⢿⢬⡾⢯⣿⣻⣿⣿⣧⣲⠿⡿⡳⡻⢿⢻⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣾⢯⣿⣟⡾⣹⡶⣯⣷⣻⡽⣿⣽⣿⣷⣿⣯⣳⡿⣗⣿⠎⠀⠀⠀⠀
⣛⡷⣧⣝⣻⣽⣿⣿⡿⣻⠋⠁⠀⡠⣔⠢⣉⣾⣯⡯⣗⣿⣞⣯⣿⣻⣽⣿⣿⣿⣯⣟⣷⣻⣷⣻⣿⣟⣿⣯⣻⣽⣷⣿⣻⡷⣟⡟⣿⣿⣿⣷⣿⡵⡗⢧⠁⠀⠀⠀⠀⠀
⠉⠁⠉⠩⣿⡽⠓⣧⢣⣁⢱⢦⣱⣏⣿⡸⣿⣺⣷⣟⣯⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡯⣿⣟⣿⣿⡽⣾⣏⢷⣽⣧⣯⣟⣾⡿⣿⣛⣷⣛⣿⠛⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⣵⣲⣷⢻⣥⡟⣿⡿⣾⣿⣟⣷⣿⣻⣷⣿⣿⣟⣿⣿⣟⣿⣟⣿⢿⣿⣯⣿⣾⡷⣿⣻⣟⣷⣿⣿⣽⣾⢏⣷⣷⣮⣷⣻⢷⣻⣞⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣯⣿⣿⣬⡏⢻⣿⣧⣿⣷⡟⣯⣿⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣽⣷⣿⣿⣯⣿⣿⣷⣯⣿⣾⣿⣽⣷⢻⣽⣾⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⢝⣞⡿⣏⡽⣪⡵⢿⣻⣽⣟⣿⡿⣟⡿⣷⣻⣽⢿⣼⣷⣻⣟⣿⣽⣾⣾⣿⣿⣿⢿⣞⣿⣻⣿⣿⣿⣿⣻⣯⣿⣿⣟⡻⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠓⠂⠧⣯⢏⡧⣿⢻⣏⣿⣿⢿⣯⣟⣾⣻⢿⣳⣯⣷⡿⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠛⠿⠜⣯⣞⣻⣾⣻⣾⣽⣿⣽⣻⡿⣟⣿⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠘⠙⠛⠓⠿⣿⡿⠿⠟⢿⣾⣿⣿⠿⠿⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                    time.sleep (0.6)
                    
                    print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣽⣯⣿⣿⣞⣦⣄⣤⣀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⢻⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣀⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣼⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣐⣿⣿⣾⣿⡿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣜⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣟⣵⣥⣦⠀⠀⠀
            ⠀⠀⠈⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣻⢻⢟⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠯⠖⠁⠀⠀
            ⠀⠀⢰⣿⣻⣿⣿⣿⣿⣿⣿⡿⣿⠿⡿⠿⠚⠊⠁⠀⠀⠀⠀⠀⠈⠉⠙⠟⢿⢿⠟⠋⠀⣤⣤⡄⠀⠀
            ⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣿⣿⣿⢿⡿⣶⣶⣿⣏⣆⠀⠀⠀
            ⠀⢀⣷⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⠂⠀⠀⠀
            ⠀⢘⣿⣿⣿⣿⣿⣿⡿⢋⣁⣄⣀⡀⠀⠀⠀⠀⣀⣶⣿⣿⣻⣿⣿⣻⣿⣿⣿⣿⣿⣿⢟⠏⠀⠀⠀⠀
            ⢠⣻⣿⣿⣿⣿⢿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣻⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀
            ⠾⠟⠛⠉⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡿⠁⠀⠀⠀⠀⠀⠀
            ⠒⢲⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠸⠿⣼⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣾⣿⣿⠿⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢓⠛⠿⠿⠿⣿⠿⠿⣿⢿⠿⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                    break

        case 2:
            print ("Ahora es de decir un chiste jiji, que le dijo la luna al sol???")
            time.sleep (2)
            print (".....")
            time.sleep (1)
            print ("De noche es batman y de día es la lindura de tus ojitos jiji")
            time.sleep (3)

        case 3:
            print ("Lo mas probable que este codigo ahora es el que me costo demasiado pero todo por ti baby <3")
        case 4:
            print ("Vuelve cuando quieras mi bebe muuuuuuuak gugu <3")
            print (''' 
                ░██▓▒░░▒▓██
                ██▓▒░__░▒▓██___██████
                ██▓▒░____░▓███▓__░▒▓██
                ██▓▒░___░▓██▓_____░▒▓██
                ██▓▒░_______________░▒▓██
                 ██▓▒░______________░▒▓██
                  ██▓▒░____________░▒▓██
                   ██▓▒░__________░▒▓██
                   ██▓▒░________░▒▓██
                    ██▓▒░_____░▒▓██
                      ██▓▒░__░▒▓██
                       █▓▒░░▒▓██
                         ░▒▓██
                        ░▒▓██
                       ''')
            break
        case _:
              print("Opción inválida. Por favor, selecciona una opción del menú.")