from recepcion import Recepcion
from farmacia import Farmacia

def menu():
    recepcion = Recepcion()
    farmacia = Farmacia()

    while True:
        print("\n--- Clínica: Menú Principal ---")
        print("1. Agregar paciente")
        print("2. Atender paciente")
        print("3. Mostrar cola de pacientes")
        print("4. Agregar medicamento")
        print("5. Entregar medicamento")
        print("6. Mostrar pila de medicamentos")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            recepcion.agregar_paciente(nombre)
        elif opcion == "2":
            recepcion.atender_paciente()
        elif opcion == "3":
            recepcion.mostrar_cola()
        elif opcion == "4":
            medicamento = input("Nombre del medicamento: ")
            farmacia.agregar_medicamento(medicamento)
        elif opcion == "5":
            farmacia.entregar_medicamento()
        elif opcion == "6":
            farmacia.mostrar_pila()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
