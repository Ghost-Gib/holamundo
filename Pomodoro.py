import tkinter as tk
from tkinter import ttk, messagebox
import time

class PomodoroApp:
    """
    Clase principal de la aplicación de Reloj Pomodoro.
    Gestiona la interfaz de usuario, la lógica del temporizador y los temas.
    """
    def __init__(self, master):
        self.master = master
        master.title("Reloj Pomodoro")
        # Establece el tamaño inicial de la ventana y la hace redimensionable.
        master.geometry("400x300")
        master.resizable(True, True) # ¡Cambiado a True, True para permitir redimensionar!

        # --- Variables de estado del temporizador ---
        self.pomodoro_time = 25 * 60  # Tiempo de Pomodoro por defecto: 25 minutos
        self.short_break_time = 5 * 60  # Tiempo de Descanso Corto por defecto: 5 minutos
        self.long_break_time = 15 * 60  # Tiempo de Descanso Largo por defecto: 15 minutos
        self.current_time_left = self.pomodoro_time # Tiempo restante actual en segundos
        self.is_running = False # Indica si el temporizador está en marcha
        self.job = None # ID del trabajo after() para poder cancelarlo
        self.current_phase = "Pomodoro" # Fase actual: "Pomodoro", "Descanso Corto", "Descanso Largo"
        self.pomodoro_count = 0 # Contador de Pomodoros completados para determinar el descanso largo

        # --- Definición de Temas (¡Ahora en tonalidades pastel!) ---
        # Cada tema es un diccionario con colores para el fondo (bg),
        # el primer plano/texto (fg), el borde y los botones.
        self.themes = {
            "Default": {
                "bg": "#E0E0E0", "fg": "#555555", "border": "#D0D0D0", # Gris pastel
                "button_bg": "#A8D8AD", "button_fg": "#333333" # Verde suave con texto oscuro
            },
            "Armonía Púrpura": {
                "bg": "#CDB4DB", "fg": "#BDECB6", "border": "#A2D2FF", # Lavanda, menta suave, azul cielo pastel
                "button_bg": "#BDECB6", "button_fg": "#CDB4DB" # Menta suave con texto lavanda
            },
            "Simple": {
                "bg": "#2C2C2C", "fg": "#F0F0F0", "border": "#F0F0F0", # Gris oscuro casi negro, gris muy claro
                "button_bg": "#F0F0F0", "button_fg": "#2C2C2C" # Gris muy claro con texto oscuro
            },
            "Atardecer": { # Fondo amarillo pastel, elementos púrpura pastel, bordes celestes pastel
                "bg": "#FFFACD", "fg": "#A569BD", "border": "#B0E0E6",
                "button_bg": "#A569BD", "button_fg": "#FFFACD"
            },
            "Océano": { # Fondo azul pastel, elementos verde pastel, bordes rojo pastel
                "bg": "#ADD8E6", "fg": "#98FB98", "border": "#FFB6C1",
                "button_bg": "#98FB98", "button_fg": "#ADD8E6"
            }
        }
        self.current_theme_name = "Default" # Tema inicial

        # --- Configuración de Estilos para Widgets ttk ---
        # Permite personalizar la apariencia de los widgets ttk (Themed Tkinter)
        self.style = ttk.Style()
        # Configura el estilo para el Frame principal (interno)
        self.style.configure("TFrame", background=self.themes[self.current_theme_name]["bg"])
        # Configura el estilo para las etiquetas (timer y fase)
        self.style.configure("TLabel", background=self.themes[self.current_theme_name]["bg"],
                             foreground=self.themes[self.current_theme_name]["fg"],
                             font=("Inter", 48, "bold")) # Fuente "Inter" y tamaño grande para el temporizador
        # Configura el estilo para los botones
        self.style.configure("TButton",
                             background=self.themes[self.current_theme_name]["button_bg"],
                             foreground=self.themes[self.current_theme_name]["button_fg"],
                             font=("Inter", 12, "bold"), # Fuente "Inter" y negrita
                             padding=10, relief="raised", borderwidth=2) # Relleno, relieve y borde
        # Define cómo se ve el botón cuando está activo (hover/clic)
        self.style.map("TButton",
                       background=[('active', self.themes[self.current_theme_name]["button_fg"])],
                       foreground=[('active', self.themes[self.current_theme_name]["button_bg"])])


        # --- Creación de la Interfaz de Usuario ---

        # Frame exterior para el borde (tk.Frame soporta 'background' para el color del borde)
        self.border_frame = tk.Frame(master, background=self.themes[self.current_theme_name]["border"], bd=2)
        self.border_frame.pack(expand=True, fill="both", padx=10, pady=10) # Añade padding para el borde visual

        # Frame principal interno que contendrá todos los elementos de la UI
        # Este es un ttk.Frame, por lo que no usaremos highlightbackground/color aquí
        self.main_frame = ttk.Frame(self.border_frame, padding="20 20 20 20", relief="solid", borderwidth=0) # Borderwidth 0 aquí
        self.main_frame.pack(expand=True, fill="both", padx=2, pady=2) # Pequeño padding para que se vea el borde del border_frame

        # Etiqueta para mostrar el tiempo restante del temporizador
        self.timer_label = ttk.Label(self.main_frame, text=self._format_time(self.current_time_left))
        self.timer_label.pack(pady=20)

        # Etiqueta para mostrar la fase actual (Pomodoro, Descanso Corto, etc.)
        self.phase_label = ttk.Label(self.main_frame, text=self.current_phase, font=("Inter", 16))
        self.phase_label.pack(pady=5)

        # Frame para agrupar los botones de control
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        # Botones de control del temporizador
        self.start_button = ttk.Button(self.button_frame, text="Iniciar", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = ttk.Button(self.button_frame, text="Pausar", command=self.pause_timer)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = ttk.Button(self.button_frame, text="Reiniciar", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.skip_button = ttk.Button(self.button_frame, text="Saltar", command=self.skip_timer)
        self.skip_button.grid(row=0, column=3, padx=5)

        # --- Creación de la Barra de Menú ---
        self._create_menu()

        # Aplica el tema inicial al iniciar la aplicación
        self.apply_theme(self.current_theme_name)


    def _create_menu(self):
        """Crea la barra de menú con opciones para tiempo y temas."""
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # Menú de Opciones de Tiempo
        time_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tiempo", menu=time_menu)
        time_menu.add_command(label="Pomodoro (25 min)", command=lambda: self.set_pomodoro_time(25))
        time_menu.add_command(label="Pomodoro (30 min)", command=lambda: self.set_pomodoro_time(30))
        time_menu.add_command(label="Descanso Corto (5 min)", command=lambda: self.set_break_time(5, "short"))
        time_menu.add_separator() # Separador visual
        time_menu.add_command(label="Descanso Largo (15 min)", command=lambda: self.set_break_time(15, "long"))
        time_menu.add_command(label="Descanso Largo (20 min)", command=lambda: self.set_break_time(20, "long"))

        # Menú de Temas
        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Temas", menu=theme_menu)
        # Itera sobre los nombres de los temas y crea un comando para cada uno
        for theme_name in self.themes.keys():
            theme_menu.add_command(label=theme_name, command=lambda name=theme_name: self.apply_theme(name))

    def _format_time(self, seconds):
        """
        Formatea una cantidad de segundos en una cadena "MM:SS".
        Ejemplo: 150 segundos -> "02:30"
        """
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def _update_timer_display(self):
        """Actualiza el texto de la etiqueta del temporizador y la fase."""
        self.timer_label.config(text=self._format_time(self.current_time_left))
        self.phase_label.config(text=self.current_phase)

    def _update_border_color(self):
        """Actualiza el color del borde del frame principal según el tema actual."""
        current_theme = self.themes[self.current_theme_name]
        # Ahora actualizamos el color de fondo del tk.Frame exterior que actúa como borde
        self.border_frame.config(background=current_theme["border"])


    def start_timer(self):
        """Inicia o reanuda el temporizador."""
        if not self.is_running:
            self.is_running = True
            self._countdown() # Inicia el conteo regresivo
            self.start_button.config(state="disabled") # Deshabilita el botón Iniciar
            self.pause_button.config(state="normal") # Habilita el botón Pausar

    def pause_timer(self):
        """Pausa el temporizador."""
        if self.is_running:
            self.is_running = False
            if self.job:
                self.master.after_cancel(self.job) # Cancela el trabajo after() pendiente
            self.start_button.config(state="normal") # Habilita el botón Iniciar
            self.pause_button.config(state="disabled") # Deshabilita el botón Pausar

    def reset_timer(self):
        """Reinicia el temporizador al tiempo inicial de la fase actual."""
        self.pause_timer() # Primero pausa el temporizador
        if self.current_phase == "Pomodoro":
            self.current_time_left = self.pomodoro_time
        elif self.current_phase == "Descanso Corto":
            self.current_time_left = self.short_break_time
        elif self.current_phase == "Descanso Largo":
            self.current_time_left = self.long_break_time
        self._update_timer_display() # Actualiza la visualización
        self.start_button.config(state="normal") # Asegura que los botones estén en estado correcto
        self.pause_button.config(state="normal")

    def skip_timer(self):
        """Salta a la siguiente fase del ciclo Pomodoro."""
        self.pause_timer() # Pausa el temporizador actual
        self._next_phase() # Avanza a la siguiente fase
        self._update_timer_display() # Actualiza la visualización
        self.start_button.config(state="normal") # Asegura que los botones estén en estado correcto
        self.pause_button.config(state="normal")


    def _countdown(self):
        """Lógica principal del conteo regresivo."""
        if self.is_running and self.current_time_left > 0:
            self.current_time_left -= 1 # Decrementa el tiempo
            self._update_timer_display() # Actualiza la pantalla
            # Llama a esta función de nuevo después de 1 segundo (1000 ms)
            self.job = self.master.after(1000, self._countdown)
        elif self.current_time_left == 0:
            self.is_running = False
            # Muestra un mensaje cuando el tiempo de la fase termina
            messagebox.showinfo("Pomodoro", f"¡Tiempo de {self.current_phase} terminado!")
            self._next_phase() # Pasa a la siguiente fase
            self._update_timer_display() # Actualiza la visualización
            # Habilita los botones al finalizar una fase
            self.start_button.config(state="normal")
            self.pause_button.config(state="normal")

    def _next_phase(self):
        """Determina la siguiente fase en el ciclo Pomodoro."""
        if self.current_phase == "Pomodoro":
            self.pomodoro_count += 1
            if self.pomodoro_count % 4 == 0: # Cada 4 Pomodoros, un descanso largo
                self.current_phase = "Descanso Largo"
                self.current_time_left = self.long_break_time
            else: # Si no, un descanso corto
                self.current_phase = "Descanso Corto"
                self.current_time_left = self.short_break_time
        elif self.current_phase in ["Descanso Corto", "Descanso Largo"]:
            # Después de un descanso, vuelve a la fase Pomodoro
            self.current_phase = "Pomodoro"
            self.current_time_left = self.pomodoro_time

    def set_pomodoro_time(self, minutes):
        """Establece el tiempo para la fase Pomodoro."""
        self.pomodoro_time = minutes * 60
        # Si la fase actual es Pomodoro y no está corriendo, actualiza el tiempo restante
        if self.current_phase == "Pomodoro" and not self.is_running:
            self.current_time_left = self.pomodoro_time
            self._update_timer_display()
        messagebox.showinfo("Configuración", f"Tiempo de Pomodoro establecido a {minutes} minutos.")

    def set_break_time(self, minutes, break_type):
        """Establece el tiempo para un descanso (corto o largo)."""
        if break_type == "short":
            self.short_break_time = minutes * 60
            # Si la fase actual es Descanso Corto y no está corriendo, actualiza el tiempo restante
            if self.current_phase == "Descanso Corto" and not self.is_running:
                self.current_time_left = self.short_break_time
                self._update_timer_display()
            messagebox.showinfo("Configuración", f"Tiempo de Descanso Corto establecido a {minutes} minutos.")
        elif break_type == "long":
            self.long_break_time = minutes * 60
            # Si la fase actual es Descanso Largo y no está corriendo, actualiza el tiempo restante
            if self.current_phase == "Descanso Largo" and not self.is_running:
                self.current_time_left = self.long_break_time
                self._update_timer_display()
            messagebox.showinfo("Configuración", f"Tiempo de Descanso Largo establecido a {minutes} minutos.")

    def apply_theme(self, theme_name):
        """
        Aplica el tema seleccionado a todos los widgets de la aplicación.
        Cambia los colores de fondo, primer plano, botones y bordes.
        """
        self.current_theme_name = theme_name
        theme_colors = self.themes[theme_name]

        # Actualiza las configuraciones de estilo de ttk
        self.style.configure("TFrame", background=theme_colors["bg"])
        self.style.configure("TLabel", background=theme_colors["bg"],
                             foreground=theme_colors["fg"])
        self.style.configure("TButton",
                             background=theme_colors["button_bg"],
                             foreground=theme_colors["button_fg"])
        # Actualiza el mapeo de colores para el estado activo de los botones
        self.style.map("TButton",
                       background=[('active', theme_colors["button_fg"])],
                       foreground=[('active', theme_colors["button_bg"])])

        # Aplica los cambios a la ventana raíz y a los widgets existentes
        self.master.config(bg=theme_colors["bg"]) # Cambia el fondo de la ventana principal
        self.main_frame.config(style="TFrame") # Reaplica el estilo al frame principal
        self.timer_label.config(style="TLabel") # Reaplica el estilo a la etiqueta del temporizador
        self.phase_label.config(style="TLabel") # Reaplica el estilo a la etiqueta de fase
        # Itera sobre los botones y reaplica el estilo
        for widget in self.button_frame.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.config(style="TButton")

        self._update_border_color() # Actualiza el color del borde del frame principal
        messagebox.showinfo("Tema", f"Tema '{theme_name}' aplicado.")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk() # Crea la ventana principal de Tkinter
    app = PomodoroApp(root) # Instancia la aplicación Pomodoro
    root.mainloop() # Inicia el bucle de eventos de Tkinter
