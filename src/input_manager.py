"""
Aqui tendremos toda la logica para manejar las entradas de los dispositivos 

"""
from inputs import get_gamepad
class GamepadManger:
        def __init__(self):
                #creamos un diccionario llamado estdo actual donde guardo los primeros botonoes a detectar 
             self.estado_actual = {
            "BTN_SOUTH": 0,  # Botón Acción (X en PS4)
            "BTN_NORTH": 0,  # Botón Saltar (Triángulo)
            "ABS_X": 0,      # Stick Izquierdo (Horizontal)
            "ABS_Y": 0,      # Stick Izquierdo (Vertical)
            "ABS_Z": 0,       # Gatillos (L2/R2)
            "BTN_EAST": 0,    # Círculo
            "BTN_WEST": 0,    # Cuadrado
            "BTN_TL": 0,      # L1
            "BTN_TR": 0,      # R1
            "ABS_HAT0X": 0,   # Flechas Horizontales
            "ABS_HAT0Y": 0    # Flechas Verticales
        }
             self.zona_muerta = 2000
             
        def polling(self):
            try:
                lista_eventos = get_gamepad()  #obtengo la list  de eventos
                
            
                for event in lista_eventos:  #  Recorroz cada evento
                    if event.code in self.estado_actual:
                        # Lógica para los Sticks Analógicos
                        if event.code.startswith("ABS_X") or event.code.startswith("ABS_Y"): 
                            if abs(event.state) > self.zona_muerta:
                                self.estado_actual[event.code] = event.state
                            else:
                                self.estado_actual[event.code] = 0
                        
                        else:
                            self.estado_actual[event.code] = event.state
            except Exception:
                pass

        def obtener_estado(self):
            """Retorna el estado actual para que main.py lo lea."""
            return self.estado_actual