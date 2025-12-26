from src.input_manager import GamepadManger
import time

def test_stick():
    try:
        mando = GamepadManger()
    except Exception as e:
        print("Conecta el mando, porfa.")
        return

    print("--- MODO TEST DE STICK ---")
    print("Mueve el stick a los lados.")
    print("Pulsa Ctrl+C para salir.")
    print("--------------------------")

    while True:
        mando.polling()
        estado = mando.obtener_estado()
        
        # Leemos el eje X (Horizontal)
        valor_x = estado["ABS_X"]
        
        # Leemos el eje Y (Vertical) también por si quieres ver los dos
        valor_y = estado["ABS_Y"]
        
        # Imprimimos bonito
        print(f"X (Lados): {valor_x}  |  Y (Arriba/Abajo): {valor_y}")
        
        # Ponemos un sleep para que te dé tiempo a leer los números
        time.sleep(0.2)

if __name__ == "__main__":
    test_stick()