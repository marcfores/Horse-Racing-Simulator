import random
import art
import time
# random: generación de números aleatorios (simulación lanzamiento de dados)
# art: creación de arte ASCII
# time: utilidad en eventos narrativos

# CLASE 1
class CarreraDeCaballos: # Clase que representa el juego de la carrera (encapsula la lógica de jugabilidad)
    def __init__(self, jugadores):
        # Inicialización de la clase con la lista de jugadores y sus posiciones
        self.jugadores = jugadores
        self.posiciones = {jugador: 0 for jugador in jugadores} # Todas las posiciones a 0 


    def lanzar_dado(self):
        # Método que simula el lanzamiento de un dado virtual con valores entre 0 y 2
        return random.randint(0, 2)


    def jugar_turno(self):
        # Método que simula un turno de juego para cada jugador
        for jugador in self.jugadores:
            input(f"Pulsa Enter para lanzar el dado, {jugador}...")
            avance = self.lanzar_dado() # Avance individual aleatorio en el tablero
            self.posiciones[jugador] += avance


    def comprobar_ganador(self):
        # Método que verifica si algún jugador ha alcanzado o superado la posición 20
        for jugador, posicion in self.posiciones.items():
            if posicion >= 20:
                return jugador
        return None # Si hay un ganador, devuelve el nombre; contrariamente, None


    def mostrar_tablero(self, caballos_jugadores): # Se añade el parámetro para una posterior selección de caballo
        # Método que imprime las posiciones de los jugadores en el tablero
        print("\nPosiciones: \n")
        for jugador, posicion in self.posiciones.items():
            caballo = Caballo(jugador, "Normal")  # Crear un caballo con tipo "Normal" temporalmente
            tipo_caballo = caballos_jugadores[jugador] # Obtener el tipo de caballo del diccionario
            caballo.tipo = tipo_caballo # Establecer el tipo de caballo
            print(f"{jugador}: {caballo.dibujar_caballo() * posicion}X")
            print("\n")


# CLASE 2
class RankingJuego: # Clase que gestiona el ranking (seguimiento de puntuaciones)
    def __init__(self, nombre_archivo='ranking.txt'):
        """
        Inicializa el ranking del juego con un diccionario vacío para almacenar las puntuaciones de los jugadores.
        Además, carga los datos del ranking desde un archivo de texto si existe (se crea en caso contrario)
        """
        self.puntuaciones_jugadores = {} # Inicialización de diccionario vacío sobre las puntuaciones
        self.nombre_archivo = nombre_archivo # Por defecto, archivo 'ranking.txt'
        try: # Intenta cargar el ranking desde un archivo específico
            with open(self.nombre_archivo, 'r') as f:
                for linea in f:
                    nombre_jugador, puntuacion = linea.strip().split(':')
                    self.puntuaciones_jugadores[nombre_jugador] = int(puntuacion) # Almacenamiento en el diccionario
        except FileNotFoundError: # Si no existe el archivo, se crea uno nuevo
            open(self.nombre_archivo, 'a')


    def agregar_puntuacion(self, nombre_jugador, puntuacion):
        """
        Agrega una puntuación al total de puntos de un jugador.

        :parámetro nombre_jugador: El nombre del jugador.
        :parámetro puntuacion: La puntuación a agregar.
        """
        if nombre_jugador in self.puntuaciones_jugadores: # Si está en el ranking, suma de puntuación a la ya existente
            self.puntuaciones_jugadores[nombre_jugador] += puntuacion # Añadir al diccionario
        else: # Si no, crea una nueva entrada para ese jugador
            self.puntuaciones_jugadores[nombre_jugador] = puntuacion # Añadir al diccionario


    def obtener_ranking(self):
        """
        Devuelve el ranking actual como una lista de tuplas.

        Cada tupla contiene el nombre de un jugador y su puntuación total.
        La lista está ordenada en orden descendente según la puntuación total.
        """
        # Ordenar los jugadores por su puntuación total en orden descendente
        jugadores_ordenados = sorted(self.puntuaciones_jugadores.items(), key=lambda x: x[1], reverse=True)
        return jugadores_ordenados


    def guardar_ranking(self):
        """
        Guarda los datos del ranking actual en un archivo de texto.
        """
        with open(self.nombre_archivo, 'w') as f:
            for nombre_jugador, puntuacion in self.puntuaciones_jugadores.items():
                f.write(f"{nombre_jugador}:{puntuacion}\n") # Escribe el nombre y su puntuación


    def salon_de_la_fama(self):
        """
        Muestra el salón de la fama con los 5 mejores jugadores y sus puntuaciones.
        """
        top_5_jugadores = self.obtener_ranking()[:5]
        print(art.text2art("Salon de la Fama")) # Encabezado decorativo
        for i, (nombre_jugador, puntuacion) in enumerate(top_5_jugadores, start=1):
            print(f"{i}. {nombre_jugador} : {puntuacion} 🏆 \n") # Muestra en formato numerado con sus puntuaciones


# CLASE 3
class HistorialJuego: # Clase que mantiene el registro de datos (partidas ganadas) sobre juegos previos
    def __init__(self, nombre_archivo='historial.txt'): # Inicialización archivo de historial       
        self.nombre_archivo = nombre_archivo
        self.puntuaciones_jugadores= {}
        
        try: # Intenta cargar los datos del historial desde ese archivo 
            with open(self.nombre_archivo, 'r') as f:  
                for linea in f:
                    nombre_jugador, puntuacion = linea.strip().split(':')
                    self.puntuaciones_jugadores[nombre_jugador] = int(puntuacion)
        except FileNotFoundError: # Si no, se crea uno nuevo
            with open(self.nombre_archivo, 'a'):  # Crear el archivo si no existe
                pass
    
    def guardar_historial(self):
        """
        Guarda el historial de juego en el archivo de historial.
        """
        if self.puntuaciones_jugadores:  # Guardar solo si hay datos para guardar
            with open(self.nombre_archivo, 'w') as f: # Modo escritura sobre el archivo especificado ('historial.txt')
                for nombre_jugador, puntuacion in self.puntuaciones_jugadores.items():
                    f.write(f"{nombre_jugador}:{puntuacion}\n") # Escribe cada entrada en una línea (nombre y puntuación)

    def agregar_puntuacion(self, nombre_jugador, puntuacion):
        """
        Agrega una puntuación al historial de juego.

        :parámetro nombre_jugador: El nombre del jugador.
        :parámetro puntuacion: La puntuación del jugador.
        """
        if nombre_jugador in self.puntuaciones_jugadores:
            self.puntuaciones_jugadores[nombre_jugador] += puntuacion # Si está en el diccionario, suma de la puntuación existente
        else:
            self.puntuaciones_jugadores[nombre_jugador] = puntuacion # Si no, nueva entrada de historial
        
        self.guardar_historial()
    
    def mostrar_historial(self):
        """
        Muestra el historial de juego con los nombres de los jugadores y sus puntuaciones
        """
        print("\nHistorial del Juego (Partidas ganadas):\n")
        if not self.puntuaciones_jugadores: # Comprueba si el historial está vacío
            print("El historial está vacío. \n") # Muestra un mensaje si el historial está vacío
        else:
            for jugador, puntuacion in self.puntuaciones_jugadores.items():
                print(f"{jugador}: {puntuacion}\n")  # Imprime cada jugador y su puntuación
                

# CLASE 4
class ObstaculoPotenciador: # Clase para la generación de eventos aleatorios (obstáculos/potenciadores)
    def __init__(self):
        self.tipos = ["Obstáculo", "Potenciador"] # 2 posibles eventos

    def generar_evento(self):
        tipo_evento = random.choice(self.tipos) # Selección aleatoria entre los dos tipos definidos
        if tipo_evento == "Obstáculo":
            return "¡Has encontrado un obstáculo! Tu caballo se ha ralentizado."
        elif tipo_evento == "Potenciador":
            return "¡Has encontrado un potenciador! Tu caballo se ha acelerado." # Mensajes informativos


# CLASE 5 (En relación con la 4)
class CarreraDeCaballosConEventos(CarreraDeCaballos): # En caso de jugar con eventos, ...
    def __init__(self, jugadores):
        super().__init__(jugadores)
        self.obstaculo_potenciador = ObstaculoPotenciador() # Llamada a la clase anterior
        self.caja_sorpresa = CajaSorpresa()  # Agregar la instancia de CajaSorpresa

    def jugar_turno(self): # Al jugar un turno, ...
        for jugador in self.jugadores:
            input(f"Pulsa Enter para lanzar el dado, {jugador}...")
            avance = self.lanzar_dado()
            self.posiciones[jugador] += avance
            # Decidir aleatoriamente si se genera un evento en este turno
            if random.random() < 0.3:  # Por ejemplo, el 30% de las veces habrá un evento
                evento = self.obstaculo_potenciador.generar_evento()
                print(evento)
                if evento == "¡Has encontrado un obstáculo! Tu caballo se ha ralentizado.":
                    self.posiciones[jugador] -= 2  # Reducir el avance debido al obstáculo
            elif random.random() < 0.1:  # Probabilidad del 10% de encontrar una caja sorpresa
                evento_caja = self.caja_sorpresa.canjear()
                print(evento_caja)
                if "impulso de velocidad adicional" in evento_caja:
                    self.posiciones[jugador] += 3  # Añadir un impulso de velocidad adicional
                elif "obstáculo" in evento_caja:
                    self.posiciones[jugador] -= 2  # Ralentizar al jugador por encontrar un obstáculo
                elif "atajo secreto" in evento_caja:
                    self.posiciones[jugador] += 5  # Avanzar varias casillas hacia adelante por encontrar un atajo

# CLASE 6
class Apuestas: # Clase para realización de apuestas previas a cada carrera
    def __init__(self, jugadores, monedas_disponibles= 100):
        """
        Inicializa la clase de apuestas con la lista de jugadores y un diccionario vacío para almacenar las apuestas.
        
        :parámetro jugadores: Lista de nombres de los jugadores que participan en la carrera.
        :parámetro monedas_disponibles: Número total de monedas disponibles para realizar apuestas (por defecto 100).
        """
        self.jugadores = jugadores
        self.monedas_disponibles = monedas_disponibles
        self.apuestas = {jugador: 0 for jugador in jugadores}
        print(f"\n\033[3m¡Tienes {monedas_disponibles} monedas disponibles para repartir entre los jugadores en las apuestas!\033[0m")

    def realizar_apuestas(self):
        print("\nRealiza tus apuestas:")
        for jugador in self.jugadores:
            while True:
                try:
                    apuesta = int(input(f"Ingrese la cantidad de la apuesta para {jugador}: ")) # Por jugador, una cantidad deseada
                    if apuesta < 0:
                        raise ValueError("La apuesta no puede ser negativa.")
                    elif apuesta > self.monedas_disponibles:
                        print(f"La apuesta no puede ser mayor que las monedas disponibles ({self.monedas_disponibles}).")
                    else:
                        self.apuestas[jugador] = apuesta
                        self.monedas_disponibles -= apuesta
                        break
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

    def mostrar_apuestas(self): # Muestra de las apuestas realizadas
        print("\nApuestas realizadas:")
        for jugador, apuesta in self.apuestas.items():
            print(f"{jugador}: ${apuesta}")

    def obtener_ganadores(self, ganador): # Obtiene la lista de ganadores y sus respectivas apuestas
        ganadores = []
        for jugador, apuesta in self.apuestas.items():
            if ganador == jugador:
                ganadores.append((jugador, apuesta))
        return ganadores # Lista de tuplas (nombre y apuesta) de los jugadores que apostaron


# CLASE 7
class NarrativaJuego: # Clase adicional para insertrar una cierta narrativa durante el juego
    def __init__(self):
        # Definir diferentes eventos narrativos centrados en la competencia de la carrera de caballos
        self.eventos = [
            "Los caballos se alinean en la pista. La multitud aguarda expectante",
            "Los jinetes ajustan las riendas con determinación mientras los caballos se preparan para esta arrancada",
            "Los corredores parten a toda velocidad, dejando un rastro de polvo tras ellos",
            "Una curva cerrada se aproxima, desafiando la habilidad de los jinetes para mantener el control",
            "Un corredor toma la delantera mientras los demás luchan por alcanzarlo. La competencia se intensifica",
            "Los jinetes se esfuerzan al máximo en la recta, buscando cruzar la meta en primer lugar y alcanzar la gloria",
            "Un caballo tropezó, pero su jinete logra mantener el control y sigue en la carrera",
            "Se levanta una leve brisa, agitando las crines de los caballos y añadiendo un desafío adicional para los jinetes",
            "Un espectador exaltado anima a su favorito desde las gradas, creando aún más tensión en el ambiente",
            "La pista se torna resbaladiza debido a la lluvia reciente, obligando a los jinetes a ser aún más cautelosos",
            "Un caballo rezagado da un sorprendente esprint, demostrando que la carrera aún está llena de giros inesperados",
            "Un jinete intenta adelantar a otro por el interior en una maniobra arriesgada, desatando el suspenso entre los espectadores",
            "Un corredor se desvía del camino establecido, buscando una ruta alternativa para ganar terreno",
            "Un caballo muestra signos de cansancio, pero su jinete lo alienta y continúa la carrera con determinación",
            "Un grupo de pájaros sobrevuela la pista, distrayendo momentáneamente a los caballos y sus jinetes",
            "Una nube de polvo se levanta tras los caballos, dificultando la visión de los jinetes y aumentando la incertidumbre",
            "Un caballo relincha nervioso, contagiando su nerviosismo al resto de los competidores",
            "Un jinete realiza un movimiento audaz para bloquear el avance de un competidor cercano, desencadenando protestas y discusiones",
            "Un rayo ilumina el cielo en medio de la carrera, añadiendo un elemento de peligro y drama",
            "Un caballo se detiene de repente, desconcertando a su jinete y causando un frenesí entre los otros competidores"
        ]

    def mostrar_evento(self):
        evento = random.choice(self.eventos) # Muestra de un evento aleatorio 
        print("\n")
        for letra in evento:
            print(letra, end="", flush=True)
            time.sleep(0.02)  # Agregar un pequeño retraso para un efecto de escritura
        print("\n")
  

# CLASE 8
class Caballo: # Clase para elegir un tipo de caballo
    tipos = {
        "Normal": "🐴",
        "Rápido": "🏇",
        "Fuerte": "🐎",
        "Ágil": "🐲"
    } # Generación de un diccionario con diferentes tipos a elegir de caballos (Nombre y dibujo)

    def __init__(self, nombre, tipo): # Inicialización de un objeto Caballo con nombre y tipo asociados
        self.nombre = nombre
        self.tipo = tipo 
    
    def dibujar_caballo(self): # Devuelve la representación gráfica correspondiente al tipo de caballo
        return Caballo.tipos[self.tipo]

    def elegir_tipo_caballo(): # Parte iterativa con el usuario
        print("\nElige un tipo de caballo:")
        for i, tipo in enumerate(Caballo.tipos, 1):
            print(f"{i}. {tipo}") # Muestra los tipos de caballo a elegir
        while True:
            try:
                opcion = int(input("Ingresa el número correspondiente al tipo de caballo: ")) # Pregunta por el deseado para cada jugador
                if 1 <= opcion <= len(Caballo.tipos):
                    return list(Caballo.tipos.keys())[opcion - 1]
                else:
                    print("Opción inválida. Por favor, ingresa un número dentro del rango.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
                

# CLASE 9
class CajaSorpresa: # Clase sobre cajas sorpresa que influyen al juego
    def __init__(self):
        self.eventos = [
            "\033[3m¡Has encontrado una caja sorpresa! Obtienes un impulso de velocidad adicional.\033[0m",
            "\033[3m¡Abres una caja sorpresa y encuentras un obstáculo! Tu caballo se ralentiza momentáneamente.\033[0m",
            "\033[3mDentro de la caja sorpresa, encuentras un atajo secreto. Avanzas varias casillas hacia adelante.\033[0m"
        ]

    def canjear(self):
        return random.choice(self.eventos) # Selección aleatoria de un evento (entre los 3 definidos)


# CLASE 10 (FUNCIONALIDAD 4)
class EntrenamientoCaballos: # Clase alternativa para simular una especie de entrenamiento
    def __init__(self, jugadores):
        self.jugadores = jugadores

    def jugar_entrenamiento(self): # Opciones inicales para el usuario sobre posibles entrenamientos
        print("\nSelecciona el tipo de entrenamiento:")
        print("1. Entrenamiento de preguntas y respuestas")
        print("2. Juego de velocidad: salto de obstáculos")
        opcion = input("Ingresa tu elección: ")

        if opcion == "1":
            self.entrenamiento_preguntas_respuestas()
        elif opcion == "2":
            self.otro_juego_entrenamiento() # Dependiendo de la elección, se llama a la función pertinente
        else:
            print("Opción inválida. Volviendo al menú principal.\n")

    def entrenamiento_preguntas_respuestas(self):
        print("\n\033[3m¡Bienvenido al Entrenamiento de Preguntas y Respuestas sobre Caballos!\033[0m")
         # Lista de preguntas y respuestas sobre caballos 
        preguntas_respuestas = {
        "¿Cuál es el color más común del pelaje de un caballo?": ["Marrón","Marron"],
        "¿Qué animal es utilizado comúnmente como compañero del caballo?": ["Perro"],
        "¿Qué animal es el enemigo natural del caballo?": ["Lobo"],
        "¿Cuál es el nombre de la madre del caballo?": ["Yegua"],
        "¿Cuál es el nombre de la cría de un caballo?": ["Potro"],
        "¿Qué edad tiene un caballo si es un año más viejo que un año hace un año?": ["Dos años","Dos"],
        "¿Cuál es la principal fuente de alimento para los caballos?": ["Hierba","Heno"],
        "¿Qué tipo de animal es un caballo?": ["Herbívoro","Herbivoro"],
        "¿Cuál es la parte más larga del cuerpo de un caballo?": ["Lomo"],
        "¿Cuál es la principal función de las herraduras en los caballos?": ["Proteger las pezuñas"]
        } # Se establecen, para cada pregunta, diferentes respuestas válidas según el criterio de escritura del usuario

        num_preguntas = 5  # Número de preguntas que se realizarán
        puntuacion = 0 # Puntuación inicial del jugador

        for _ in range(num_preguntas): # Iterar a través de las preguntas
            pregunta, respuesta = random.choice(list(preguntas_respuestas.items())) # Seleccionar una pregunta aleatoria y su lista de respuestas
            print("\nPregunta:", pregunta)
        
            respuesta_jugador = input("Respuesta: ").strip().capitalize() # Obtener la respuesta del jugador (capitalize() establece en mayúscula la letra inicial)
            if respuesta_jugador in respuesta:
                print("¡Respuesta correcta!")
                puntuacion += 1
            else:
                print("Respuesta incorrecta. La respuesta correcta es:", respuesta[0]) # Si no es correcta, se muestra solo el primer elemento de la lista (1 respuesta, no todas)

        print("\n¡Entrenamiento completado!")
        print(f"Puntuación final: {puntuacion}/{num_preguntas}\n") # Mostrar la puntuación final del jugador

    def otro_juego_entrenamiento(self):
        print("\n\033[3m¡Bienvenido al Juego de Salto de Obstáculos!\033[0m")

        # Definir una serie de obstáculos con alturas aleatorias
        obstaculos = [random.randint(1, 5) for _ in range(5)]  # Generar 5 obstáculos aleatorios de alturas entre 1 y 5

        print("¡Prepárate para saltar los obstáculos!")
        time.sleep(2)
        tiempo_inicio = time.time()  # Registrar el tiempo de inicio del juego
        
        puntuacion= 0
        # Iterar a través de los obstáculos (enumerate - contador a un iterable devolviéndolo como objeto enumerado)
        for i, altura in enumerate(obstaculos, start=1):
            print(f"\nObstáculo {i}: Adivina la altura del obstáculo")
            altura_salto = int(input("Ingrese la altura de salto de su caballo (1-5): "))
        
            # Verificar si el caballo supera el obstáculo
            if altura_salto == altura:
                puntuacion+= 1
                print(f"¡La altura del obstáculo era {altura}!")
                print("¡Salto exitoso!")
            else:
                print(f"¡La altura del obstáculo era {altura}!")
                print("¡El caballo no pudo superar el obstáculo!")

        tiempo_final = time.time()  # Registrar el tiempo al finalizar el juego
        tiempo_total = tiempo_final - tiempo_inicio  # Calcular el tiempo total transcurrido

        # Mostrar el tiempo total y la puntuación
        print("\n¡Juego completado!")
        print(f"Tiempo total: {tiempo_total:.2f} segundos")
        print (f"Puntuación final: {puntuacion}/5\n")

# CLASE 11   
class GameManager: # Clase principal que maneja la lógica del juego
    def __init__(self):
        self.ranking = RankingJuego()  # Instancia para gestionar el ranking del juego
        self.historial = HistorialJuego()  # Instancia para mantener el historial del juego
        self.narrativa = NarrativaJuego()  # Instancia para manejar la narrativa del juego
        self.juego = None  # Esta será la instancia del juego actual (se establecerá más adelante)
        self.jugadores = []  # Lista de nombres de jugadores
        self.caballos_jugadores = {}  # Diccionario para almacenar los tipos de caballos elegidos por los jugadores

    def mostrar_bienvenida(self):
        bienvenida = art.text2art("Bienvenido\nal Juego de\nCarreras de\nCaballos", "random", False)
        print(bienvenida) # Imprime mensaje de bienvenida usando la librería de arte

    def manejar_menu_principal(self):
        while True:
            print("Por favor, selecciona una opción:")
            print("1. Comenzar un nuevo juego")
            print("2. Salón de la Fama")
            print("3. Historial del Juego")
            print("4. Entrenamiento de Caballos")
            print("5. Salir")

            entrada_jugador = input("Ingresa tu elección: ")

            if entrada_jugador == "1": # Dependiendo de la elección del usuario, acciones específicas
                self.comenzar_nuevo_juego()
                break # Sale del bucle
            elif entrada_jugador == "2":
                self.ranking.salon_de_la_fama() # Devuelve el salón de la fama  
            elif entrada_jugador == "3":
                self.historial.mostrar_historial() # Llama al método para mostrar el historial de juego
            elif entrada_jugador == "4":
                self.realizar_entrenamiento() # Comienza la Clase de Entrenamiento de caballos
            elif entrada_jugador == "5":
                print("\nGracias por jugar. ¡Hasta luego!")
                exit() # Termina la ejecución del programa

    def comenzar_nuevo_juego(self):
        manejo_num_jugadores = True

        while manejo_num_jugadores:
            try:
                num_jugadores = int(input("Ingresa el número de jugadores (entre 2 y 10): "))
                if 2 <= num_jugadores <= 10:
                    manejo_num_jugadores = False
                else:
                    print("El número de jugadores debe estar entre 2 y 10. Por favor, inténtalo de nuevo.")
            except ValueError: # Excepción en caso de solicitud errónea
                print("Por favor, ingresa un número entre 2 y 10. Por favor, inténtalo nuevamente.")

        self.jugadores = [input(f"Ingresa el nombre del jugador {i+1}: ") for i in range(num_jugadores)]

        apuestas = Apuestas(self.jugadores)
        apuestas.realizar_apuestas()
        # Momento de realizar apuestas
        
        # Preguntar al usuario si quiere jugar con eventos
        jugar_con_eventos = input("¿Quieres activar los eventos durante la carrera? (s/n): ").lower()
        if jugar_con_eventos == "s":
            self.juego = CarreraDeCaballosConEventos(self.jugadores) # Utilizar la versión con eventos
        else:
            self.juego = CarreraDeCaballos(self.jugadores) # Utilizar la versión sin eventos

        apuestas.mostrar_apuestas() # Muestra de las apuestas, y listos para jugar

        self.caballos_jugadores = {} # Diccionario para almacenar los tipos de caballos elegidos por los jugadores
        for jugador in self.jugadores:
            tipo_caballo = Caballo.elegir_tipo_caballo()
            self.caballos_jugadores[jugador] = tipo_caballo
        
        # Sorteo del orden de los jugadores
        random.shuffle(self.jugadores)
        print(f"\nEl orden de tirada al inicio será: {', '.join(self.jugadores)}\n")

        self.jugar_carrera()

    def jugar_carrera(self):
        while True: # Simulación de los turnos de juego hasta alcanzar un ganador
            # En cada iteración:
            continuar = input("Presiona 'Enter' para jugar un turno o 'p' para pausar la partida: ")
            if continuar.lower() == "p":
                input("Partida pausada. Presiona 'Enter' para continuar...")
                continue # Vuelve al inicio del bucle para permitir al jugador pausar la partida

            self.narrativa.mostrar_evento()
            self.juego.jugar_turno() # Juego de un turno
            self.juego.mostrar_tablero(self.caballos_jugadores) # Muestra del tablero
            ganador = self.juego.comprobar_ganador() # Verificación del ganador

            if ganador: # Si lo hay, actualización del ranking con puntuaciones correspondientes
                print(f"\033[1m¡{ganador} ha ganado la carrera!\033[0m\n")
                for jugador in self.jugadores:
                    if jugador == ganador:
                        self.ranking.agregar_puntuacion(jugador, 30)
                    else:
                        self.ranking.agregar_puntuacion(jugador, -10) # Sistema de puntuaciones en el ranking
                self.ranking.guardar_ranking()
                self.historial.agregar_puntuacion(ganador, 1) # Añadir puntuación al historial para el ganador
                self.historial.guardar_historial()
                break

    def realizar_entrenamiento(self):
        entrenamiento = EntrenamientoCaballos(self.jugadores)
        entrenamiento.jugar_entrenamiento()

    def iniciar(self):
        self.mostrar_bienvenida()
        while True:
            self.manejar_menu_principal()


if __name__ == "__main__":
    # Bloque que ejecuta la función principal si el script se ejecuta directamente
    game_manager = GameManager()
    game_manager.iniciar()