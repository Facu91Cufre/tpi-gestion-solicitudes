class Estudiante:
    def __init__(self, legajo, nombre):
        self.legajo = legajo
        self.nombre = nombre

class Responsable:
    def __init__(self, id_responsable, nombre_area):
        self.id_responsable = id_responsable
        self.nombre_area = nombre_area

class Solicitud:
    def __init__(self, id_solicitud, estudiante, tipo, descripcion):
        self.id_solicitud = id_solicitud
        self.estudiante = estudiante
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = "Pendiente"
        self.responsable = None

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["Pendiente", "En Proceso","Aprobada", "Rechazada"]:
            self.estado = nuevo_estado
        else:
            print("Estado no válido.")

    def asignar_responsable(self, responsable):
        self.responsable = responsable
        self.estado = "En Proceso"