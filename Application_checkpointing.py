import pickle
import os
import time


class ApplicationState:
    def __init__(self):
        self.counter = 0
        self.data = []

    def __str__(self):
        return f"Estado actual: Contador = {self.counter}, Datos = {self.data}"


def save_checkpoint(state, filename="checkpoint.pkl"):
    """Guarda el estado actual de la aplicación"""
    with open(filename, "wb") as f:
        pickle.dump(state, f)
    print("\nCheckpoint guardado exitosamente")


def load_checkpoint(filename="checkpoint.pkl"):
    """Carga el último estado guardado"""
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            state = pickle.load(f)
        print("\nCheckpoint cargado exitosamente")
        return state
    return None


def main():
    # Intentar cargar checkpoint existente
    state = load_checkpoint()

    # Si no existe checkpoint, crear nuevo estado
    if not state:
        state = ApplicationState()
        print("Iniciando nueva ejecución")
    else:
        print("Reanudando ejecución desde checkpoint")

    print(state)

    # Simular procesamiento con checkpointing automático
    try:
        while state.counter < 100:
            # Realizar algún cálculo
            state.data.append(state.counter ** 2)

            # Mostrar progreso
            print(f"\nProcesando iteración {state.counter}...")
            time.sleep(0.5)  # Simular trabajo

            # Guardar checkpoint cada 5 iteraciones
            if state.counter % 5 == 0 and state.counter > 0:
                save_checkpoint(state)

            state.counter += 1

        # Eliminar checkpoint al completar
        if os.path.exists("checkpoint.pkl"):
            os.remove("checkpoint.pkl")
        print("\nProceso completado exitosamente")

    except KeyboardInterrupt:
        print("\nInterrupción recibida. Guardando checkpoint final...")
        save_checkpoint(state)


if __name__ == "__main__":
    main()