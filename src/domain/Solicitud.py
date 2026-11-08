from src.domain.Estados import EstadoSolicitud
from src.domain.Estudiante import Estudiante
from src.domain.Responsable import Responsable


class Solicitud:
    def __init__(self, id_solicitud: int, estudiante: Estudiante, tipo: str, descripcion: str):
        self.id_solicitud = id_solicitud
        self.estudiante = estudiante
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = EstadoSolicitud.PENDIENTE
        self.responsable = None

    def cambiar_estado(self, nuevo_estado: str):
        self.estado = EstadoSolicitud(nuevo_estado)

    def asignar_responsable(self, responsable: Responsable):
        self.responsable = responsable
        self.estado = EstadoSolicitud.EN_PROCESO