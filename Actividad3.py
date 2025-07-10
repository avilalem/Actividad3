from collections import deque

class Recepcion:
    def __init__(self):
        self.cola_pacientes=deque()
    def agregar_paciente(self,nombre):
        self.cola_pacientes.append(nombre)
        print(f"Paciente {nombre} agregado")
    def atender_paciente(self, nombre, paciente=None):
        if self.cola_pacientes:
            self.cola_pacientes.popleft()
            print(f"Paciente {nombre} atendido")
            return paciente
        else:
            print("No hay pacientes en cola")

    def mostrar_cola (self):
        if self.cola_pacientes:
            print("Pacientes en espera")
            for paciente in self.cola_pacientes:
                print (f"- {paciente}")
        else:
            print("No hay pacientes en cola")