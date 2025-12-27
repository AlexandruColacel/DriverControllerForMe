# DriverControllerForMe

Un controlador de input personalizado escrito en Python para mapear mandos modernos (XInput/PS4) a controles de teclado y ratón. Diseñado para dar soporte a videojuegos legacy (como Gothic 1 & 2) que no soportan nativamente joysticks modernos.

## 🛠️ Cómo funciona

Este driver actúa como un *middleware* de baja latencia entre el hardware del mando y el sistema operativo:

1.  **Input Polling:** La clase `GamepadManager` captura eventos del mando en tiempo real utilizando la librería `inputs`.
2.  **Deadzone Filter:** Implementa lógica de zonas muertas (Deadzone) configurable para eliminar el "drift" de los sticks analógicos desgastados.
3.  **State Machine:** Mantiene un registro del estado de las teclas para evitar la saturación del búfer de Windows ("teclas pegadas").
4.  **Mapping:** Traduce coordenadas analógicas (Ejes X/Y) a pulsaciones digitales (WASD) mediante `pydirectinput`.

## 🚀 Instalación

1.  Clona el repositorio.
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ejecuta el driver (requiere permisos de Administrador para inyectar teclas en juegos a pantalla completa):
    ```bash
    python main.py
    ```

## 📋 Requisitos

* Python 3.x
* Librerías listadas en `requirements.txt`
* Permisos de Administrador (Windows)
* Si usas mando de PS4 es necesario instalar DS4Windows

## 🔮 Roadmap

* [x] Movimiento básico (WASD) con zonas de sensibilidad.
* [ ] Control de cámara (Mapeo de Stick Derecho a Ratón).
* [ ] Mapeo de botones de acción.
* [ ] Migración futura a lenguajes de bajo nivel (Rust/Zig) para optimización de rendimiento.