from inputs import GamePad
from src.input_manager import GamepadManger
import pydirectinput
import time
def main():
    pydirectinput.FAILSAFE = True
    pydirectinput.PAUSE = 0
    
    try:
        mando = GamepadManger()
    except Exception as e:
        print("Error: Conecta el mando.")
        return
    
    print("--- DRIVER LISTO ---")
    print("Stick Arriba: W | Stick Abajo: S | Centro: Quieto")
    
    w_press = False
    s_press = False 

    a_press = False
    d_press = False
   
    ZONA_ACCION = 10000 
    ZONA_MUERTA = 5000

    while True:
        mando.polling()
        estado = mando.obtener_estado()
        valor_y = estado["ABS_Y"]
        valor_x = estado["ABS_X"]
        
        
        if valor_y > ZONA_ACCION:
            if not w_press:
                pydirectinput.keyDown('w')
                w_press = True
            
            
            if s_press:
                pydirectinput.keyUp('s')
                s_press = False

        
        # Si el valor es MAYOR que 10000 (ej: 30000)
        elif valor_y < -ZONA_ACCION:
            if not s_press:
                pydirectinput.keyDown('s') # Pulsamos S
                s_press = True
            
            # Seguridad: Soltamos W
            if w_press:
                pydirectinput.keyUp('w')
                w_press = False

       
        # Si el valor está entre -5000 y 5000, soltamos todo
        elif abs(valor_y) < ZONA_MUERTA:
            if w_press:
                pydirectinput.keyUp('w')
                w_press = False
            if s_press:
                pydirectinput.keyUp('s')
                s_press = False




    #ZONA AD
        if valor_x < -ZONA_ACCION:
            if not a_press:
                pydirectinput.keyDown('a')
                a_press = True
            
            if d_press:
                pydirectinput.keyUp('d')
                d_press = False
        
        if valor_x > ZONA_ACCION:
            if not d_press:
                pydirectinput.keyDown('d')
                d_press = True
            
            if a_press:
                pydirectinput.keyUp('a')
                a_press = False
        
        elif abs(valor_x) < ZONA_MUERTA:
            if a_press:
                pydirectinput.keyUp('a')
                a_press = False
            
            if d_press:
                pydirectinput.keyUp('d')
                d_press = False

if __name__ == "__main__":
    main()